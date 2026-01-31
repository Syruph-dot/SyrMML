import mido
from typing import List, Dict, Any

class MidiReader:
    """
    MIDI文件读取器，负责解析MIDI文件的基本结构和事件
    """
    
    def __init__(self, file_path: str):
        """
        初始化MIDI读取器
        
        Args:
            file_path: MIDI文件路径
        """
        self.file_path = file_path
        self.midi = None
        self.tracks = []
        self.header_info = {}
        
    def read_file(self) -> bool:
        """
        读取MIDI文件并解析基本信息
        
        Returns:
            bool: 读取是否成功
        """
        try:
            self.midi = mido.MidiFile(self.file_path)
            self._parse_header()
            self._parse_tracks()
            return True
        except Exception as e:
            print(f"Error reading MIDI file: {e}")
            return False
    
    def _parse_header(self):
        """
        解析MIDI文件头信息
        """
        if self.midi:
            self.header_info = {
                'file_format': self.midi.type,
                'track_count': len(self.midi.tracks),
                'ticks_per_beat': self.midi.ticks_per_beat,
                'type_description': self._get_format_description(self.midi.type)
            }
    
    def _parse_tracks(self):
        """
        解析MIDI轨道信息
        """
        if self.midi:
            self.tracks = []
            for i, track in enumerate(self.midi.tracks):
                track_info = {
                    'index': i,
                    'name': track.name if hasattr(track, 'name') else f'Track {i}',
                    'event_count': len(track),
                    'events': track
                }
                self.tracks.append(track_info)
    
    def _get_format_description(self, format_type: int) -> str:
        """
        获取MIDI文件格式的描述
        
        Args:
            format_type: MIDI文件格式类型 (0, 1, 2)
            
        Returns:
            str: 格式描述
        """
        format_desc = {
            0: '单轨道格式',
            1: '同步多轨道格式',
            2: '异步多轨道格式'
        }
        return format_desc.get(format_type, f'未知格式 ({format_type})')
    
    def get_header_info(self) -> Dict[str, Any]:
        """
        获取MIDI文件头信息
        
        Returns:
            Dict[str, Any]: 头信息字典
        """
        return self.header_info
    
    def get_tracks(self) -> List[Dict[str, Any]]:
        """
        获取所有轨道信息
        
        Returns:
            List[Dict[str, Any]]: 轨道信息列表
        """
        return self.tracks
    
    def get_track_events(self, track_index: int) -> List[mido.Message]:
        """
        获取指定轨道的事件
        
        Args:
            track_index: 轨道索引
            
        Returns:
            List[mido.Message]: 轨道事件列表
        """
        if 0 <= track_index < len(self.tracks):
            return self.tracks[track_index]['events']
        return []
    
    def print_summary(self):
        """
        打印MIDI文件摘要信息
        """
        print(f"=== MIDI文件摘要 ===")
        print(f"文件路径: {self.file_path}")
        print(f"文件格式: {self.header_info.get('file_format')} - {self.header_info.get('type_description')}")
        print(f"轨道数量: {self.header_info.get('track_count')}")
        print(f"时间分辨率: {self.header_info.get('ticks_per_beat')} ticks/beat")
        
        print("\n=== 轨道信息 ===")
        for track in self.tracks:
            print(f"轨道 {track['index']}: {track['name']} - {track['event_count']} 个事件")
