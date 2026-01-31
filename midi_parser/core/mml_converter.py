from typing import List, Dict, Any
import mido

class MMLConverter:
    """
    MIDI到MML转换器，负责将MIDI事件转换为MML格式
    """
    
    def __init__(self):
        """
        初始化MML转换器
        """
        self.default_tempo = 120
        self.default_octave = 4
        self.default_length = 4  # 四分音符
    
    def convert_to_mml(self, events: List[mido.Message], ticks_per_beat: int) -> str:
        """
        将MIDI事件转换为MML格式
        
        Args:
            events: MIDI事件列表
            ticks_per_beat: 每拍的ticks数
            
        Returns:
            str: 生成的MML字符串
        """
        # 解析音符信息
        notes = self._extract_notes(events, ticks_per_beat)
        if not notes:
            return ""
        
        # 生成MML
        mml_parts = []
        current_octave = self.default_octave
        current_length = self.default_length
        current_tempo = self.default_tempo
        
        # 添加速度指令
        mml_parts.append(f"t{current_tempo}")
        
        # 添加默认八度和长度
        mml_parts.append(f"o{current_octave}")
        mml_parts.append(f"l{current_length}")
        
        # 生成音符序列
        for note in notes:
            # 转换音高
            pitch = note['note_name'].lower()
            note_octave = int(pitch[-1])
            note_pitch = pitch[:-1]
            
            # 处理八度变化
            if note_octave != current_octave:
                mml_parts.append(f"o{note_octave}")
                current_octave = note_octave
            
            # 计算音符长度
            note_length = self._calculate_note_length(note['duration'], current_tempo, ticks_per_beat)
            
            # 处理长度变化
            if note_length != current_length:
                mml_parts.append(f"l{note_length}")
                current_length = note_length
            
            # 添加音符
            mml_parts.append(note_pitch)
        
        return " ".join(mml_parts)
    
    def _extract_notes(self, events: List[mido.Message], ticks_per_beat: int) -> List[Dict[str, Any]]:
        """
        从MIDI事件中提取音符信息
        
        Args:
            events: MIDI事件列表
            ticks_per_beat: 每拍的ticks数
            
        Returns:
            List[Dict[str, Any]]: 音符信息列表
        """
        notes = []
        note_on_events = {}
        current_time = 0
        current_tempo = 500000  # 默认120 BPM
        
        for msg in events:
            current_time += msg.time
            
            if msg.type == 'set_tempo':
                current_tempo = msg.tempo
            elif msg.type == 'note_on' and msg.velocity > 0:
                # 记录音符开启事件
                key = (msg.channel, msg.note)
                note_on_events[key] = {
                    'start_time': current_time,
                    'velocity': msg.velocity,
                    'channel': msg.channel,
                    'note': msg.note
                }
            elif (msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0)):
                # 处理音符关闭事件
                key = (msg.channel, msg.note)
                if key in note_on_events:
                    note_on = note_on_events[key]
                    duration = current_time - note_on['start_time']
                    
                    # 转换为秒
                    duration_seconds = mido.tick2second(duration, ticks_per_beat, current_tempo)
                    
                    # 创建音符信息
                    note_info = {
                        'note': msg.note,
                        'note_name': self._note_number_to_name(msg.note),
                        'start_time': note_on['start_time'],
                        'end_time': current_time,
                        'duration': duration,
                        'duration_seconds': duration_seconds,
                        'velocity': note_on['velocity'],
                        'channel': msg.channel
                    }
                    notes.append(note_info)
                    del note_on_events[key]
        
        # 按开始时间排序
        notes.sort(key=lambda x: x['start_time'])
        return notes
    
    def _calculate_note_length(self, duration_ticks: int, tempo: int, ticks_per_beat: int) -> int:
        """
        计算音符长度（基于MIDI的ticks）
        
        Args:
            duration_ticks: 音符持续的ticks数
            tempo: 当前速度（微秒/拍）
            ticks_per_beat: 每拍的ticks数
            
        Returns:
            int: MML音符长度（如4=四分音符，8=八分音符等）
        """
        # 转换为拍数
        beats = duration_ticks / ticks_per_beat
        
        # 常见音符长度（拍数）
        note_lengths = {
            4: 1.0,     # 全音符
            2: 0.5,     # 二分音符
            1: 0.25,    # 四分音符
            8: 0.125,   # 八分音符
            16: 0.0625, # 十六分音符
            32: 0.03125,# 三十二分音符
            64: 0.015625# 六十四分音符
        }
        
        # 找到最接近的音符长度
        closest_length = 4
        min_diff = float('inf')
        
        for length, beat_value in note_lengths.items():
            diff = abs(beats - beat_value)
            if diff < min_diff:
                min_diff = diff
                closest_length = length
        
        return closest_length
    
    def _note_number_to_name(self, note_num: int) -> str:
        """
        将音符数字转换为音符名称
        
        Args:
            note_num: 音符数字 (0-127)
            
        Returns:
            str: 音符名称（如 C4, A#3 等）
        """
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        octave = (note_num // 12) - 1
        note_name = note_names[note_num % 12]
        return f"{note_name}{octave}"
    
    def save_mml_to_file(self, mml: str, output_path: str):
        """
        将MML保存到文件
        
        Args:
            mml: MML字符串
            output_path: 输出文件路径
        """
        with open(output_path, 'w') as f:
            f.write(mml)
    
    def convert_file(self, input_file: str, output_file: str):
        """
        转换MIDI文件为MML文件
        
        Args:
            input_file: 输入MIDI文件路径
            output_file: 输出MML文件路径
        """
        try:
            from .midi_reader import MidiReader
            
            # 读取MIDI文件
            reader = MidiReader(input_file)
            if not reader.read_file():
                return False
            
            # 获取第一个轨道的事件
            if not reader.tracks:
                return False
            
            # 转换为MML - 使用第二个轨道（如果存在），否则使用第一个轨道
            track_index = 1 if len(reader.tracks) > 1 else 0
            events = reader.tracks[track_index]['events']
            mml = self.convert_to_mml(events, reader.header_info['ticks_per_beat'])
            
            # 保存到文件
            self.save_mml_to_file(mml, output_file)
            return True
        except Exception as e:
            print(f"Error converting MIDI to MML: {e}")
            return False
