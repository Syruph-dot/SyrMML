#!/usr/bin/env python3
"""
基础MIDI解析示例
展示如何使用MidiReader读取和解析MIDI文件
"""

from midi_parser import MidiReader

def basic_midi_parse():
    """基础MIDI解析示例"""
    # 创建MidiReader实例
    reader = MidiReader("example.mid")  # 这里需要替换为实际的MIDI文件路径
    
    # 读取MIDI文件
    if reader.read_file():
        # 打印文件摘要
        reader.print_summary()
        
        # 获取并打印头信息
        header_info = reader.get_header_info()
        print("\n=== 详细头信息 ===")
        for key, value in header_info.items():
            print(f"{key}: {value}")
        
        # 获取轨道信息
        tracks = reader.get_tracks()
        print(f"\n=== 详细轨道信息 ===")
        for track in tracks:
            print(f"轨道 {track['index']}: {track['name']}")
            print(f"  事件数量: {track['event_count']}")
            print(f"  前5个事件示例:")
            
            # 打印前5个事件
            for i, event in enumerate(track['events'][:5]):
                print(f"    {i+1}. {event.type} - {event}")
    else:
        print("读取MIDI文件失败")

if __name__ == "__main__":
    basic_midi_parse()
