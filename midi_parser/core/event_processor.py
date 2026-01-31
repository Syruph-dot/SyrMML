import mido
from typing import List, Dict, Any

class EventProcessor:
    """
    MIDI事件处理器，负责分析和处理不同类型的MIDI事件
    """
    
    def __init__(self):
        """
        初始化事件处理器
        """
        self.event_stats = {
            'note_on': 0,
            'note_off': 0,
            'control_change': 0,
            'program_change': 0,
            'pitchwheel': 0,
            'meta': 0,
            'total': 0
        }
        
        self.channel_usage = {}
        self.current_tempo = 500000  # 默认120 BPM
    
    def reset_stats(self):
        """
        重置统计数据
        """
        self.event_stats = {
            'note_on': 0,
            'note_off': 0,
            'control_change': 0,
            'program_change': 0,
            'pitchwheel': 0,
            'meta': 0,
            'total': 0
        }
        self.channel_usage = {}
        self.current_tempo = 500000
    
    def process_events(self, events: List[mido.Message]) -> Dict[str, Any]:
        """
        处理MIDI事件列表
        
        Args:
            events: MIDI事件列表
            
        Returns:
            Dict[str, Any]: 处理结果和统计信息
        """
        self.reset_stats()
        processed_events = []
        current_time = 0
        
        for msg in events:
            current_time += msg.time
            self.event_stats['total'] += 1
            
            event_info = {
                'time': msg.time,
                'absolute_time': current_time,
                'type': msg.type,
                'is_meta': msg.is_meta
            }
            
            if msg.is_meta:
                self.event_stats['meta'] += 1
                event_info['details'] = self._process_meta_event(msg)
            else:
                # 更新通道使用情况
                channel = getattr(msg, 'channel', -1)
                if channel not in self.channel_usage:
                    self.channel_usage[channel] = 0
                self.channel_usage[channel] += 1
                
                # 处理不同类型的MIDI事件
                if msg.type == 'note_on':
                    self.event_stats['note_on'] += 1
                    event_info['details'] = self._process_note_on(msg)
                elif msg.type == 'note_off':
                    self.event_stats['note_off'] += 1
                    event_info['details'] = self._process_note_off(msg)
                elif msg.type == 'control_change':
                    self.event_stats['control_change'] += 1
                    event_info['details'] = self._process_control_change(msg)
                elif msg.type == 'program_change':
                    self.event_stats['program_change'] += 1
                    event_info['details'] = self._process_program_change(msg)
                elif msg.type == 'pitchwheel':
                    self.event_stats['pitchwheel'] += 1
                    event_info['details'] = self._process_pitchwheel(msg)
                else:
                    event_info['details'] = str(msg)
            
            processed_events.append(event_info)
        
        return {
            'processed_events': processed_events,
            'stats': self.event_stats,
            'channel_usage': self.channel_usage,
            'current_tempo': self.current_tempo
        }
    
    def _process_meta_event(self, msg: mido.Message) -> Dict[str, Any]:
        """
        处理元事件
        
        Args:
            msg: 元事件
            
        Returns:
            Dict[str, Any]: 处理后的元事件信息
        """
        if msg.type == 'set_tempo':
            self.current_tempo = msg.tempo
            return {
                'type': 'set_tempo',
                'tempo': msg.tempo,
                'bpm': mido.tempo2bpm(msg.tempo)
            }
        elif msg.type == 'time_signature':
            return {
                'type': 'time_signature',
                'numerator': msg.numerator,
                'denominator': msg.denominator,
                'clocks_per_click': msg.clocks_per_click,
                'notated_32nd_notes_per_beat': msg.notated_32nd_notes_per_beat
            }
        elif msg.type == 'key_signature':
            return {
                'type': 'key_signature',
                'key': msg.key
            }
        elif msg.type == 'track_name':
            return {
                'type': 'track_name',
                'name': msg.name
            }
        else:
            return {
                'type': msg.type,
                'raw': str(msg)
            }
    
    def _process_note_on(self, msg: mido.Message) -> Dict[str, Any]:
        """
        处理音符开启事件
        
        Args:
            msg: 音符开启事件
            
        Returns:
            Dict[str, Any]: 处理后的音符信息
        """
        return {
            'channel': msg.channel,
            'note': msg.note,
            'velocity': msg.velocity,
            'note_name': self._note_number_to_name(msg.note)
        }
    
    def _process_note_off(self, msg: mido.Message) -> Dict[str, Any]:
        """
        处理音符关闭事件
        
        Args:
            msg: 音符关闭事件
            
        Returns:
            Dict[str, Any]: 处理后的音符信息
        """
        return {
            'channel': msg.channel,
            'note': msg.note,
            'velocity': msg.velocity,
            'note_name': self._note_number_to_name(msg.note)
        }
    
    def _process_control_change(self, msg: mido.Message) -> Dict[str, Any]:
        """
        处理控制器变更事件
        
        Args:
            msg: 控制器变更事件
            
        Returns:
            Dict[str, Any]: 处理后的控制器信息
        """
        control_names = {
            0: 'Bank Select (MSB)',
            1: 'Modulation Wheel',
            2: 'Breath Controller',
            7: 'Volume',
            10: 'Pan',
            11: 'Expression Controller',
            64: 'Sustain Pedal',
            65: 'Portamento',
            71: 'Resonance (Timbre)',
            72: 'Release Time',
            73: 'Attack Time',
            74: 'Brightness (Filter Cutoff)',
            120: 'All Sound Off',
            121: 'Reset All Controllers',
            123: 'All Notes Off'
        }
        
        return {
            'channel': msg.channel,
            'control': msg.control,
            'value': msg.value,
            'control_name': control_names.get(msg.control, f'Controller {msg.control}')
        }
    
    def _process_program_change(self, msg: mido.Message) -> Dict[str, Any]:
        """
        处理程序变更事件
        
        Args:
            msg: 程序变更事件
            
        Returns:
            Dict[str, Any]: 处理后的程序信息
        """
        return {
            'channel': msg.channel,
            'program': msg.program
        }
    
    def _process_pitchwheel(self, msg: mido.Message) -> Dict[str, Any]:
        """
        处理音高轮事件
        
        Args:
            msg: 音高轮事件
            
        Returns:
            Dict[str, Any]: 处理后的音高轮信息
        """
        return {
            'channel': msg.channel,
            'pitch': msg.pitch
        }
    
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
    
    def get_stats(self) -> Dict[str, Any]:
        """
        获取统计信息
        
        Returns:
            Dict[str, Any]: 统计信息
        """
        return {
            'event_stats': self.event_stats,
            'channel_usage': self.channel_usage,
            'current_tempo': self.current_tempo,
            'current_bpm': mido.tempo2bpm(self.current_tempo)
        }
    
    def print_stats(self):
        """
        打印统计信息
        """
        print("=== MIDI事件统计 ===")
        for key, value in self.event_stats.items():
            if key != 'total':
                percentage = (value / self.event_stats['total']) * 100 if self.event_stats['total'] > 0 else 0
                print(f"{key}: {value} ({percentage:.1f}%)")
        
        print(f"\n总事件数: {self.event_stats['total']}")
        print(f"当前速度: {mido.tempo2bpm(self.current_tempo):.1f} BPM")
        
        print("\n=== 通道使用情况 ===")
        for channel, count in sorted(self.channel_usage.items()):
            percentage = (count / self.event_stats['total']) * 100 if self.event_stats['total'] > 0 else 0
            print(f"通道 {channel}: {count} 个事件 ({percentage:.1f}%)")
