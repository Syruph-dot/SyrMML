#!/usr/bin/env python3
"""
高级MIDI分析示例
展示如何使用EventProcessor处理和分析MIDI事件
"""

from midi_parser import MidiReader, EventProcessor

def advanced_midi_analysis():
    """高级MIDI分析示例"""
    # 创建MidiReader实例
    reader = MidiReader("example.mid")  # 这里需要替换为实际的MIDI文件路径
    
    if reader.read_file():
        # 创建EventProcessor实例
        processor = EventProcessor()
        
        # 处理第一个轨道的事件
        tracks = reader.get_tracks()
        if tracks:
            first_track = tracks[0]
            print(f"=== 分析轨道: {first_track['name']} ===")
            
            # 处理事件
            result = processor.process_events(first_track['events'])
            
            # 打印统计信息
            print("\n=== 事件统计 ===")
            processor.print_stats()
            
            # 打印详细处理结果
            print(f"\n=== 处理结果 ===")
            print(f"处理的事件数量: {len(result['processed_events'])}")
            print(f"通道使用情况: {result['channel_usage']}")
            
            # 打印前10个处理后的事件
            print(f"\n=== 前10个处理后的事件 ===")
            for i, event in enumerate(result['processed_events'][:10]):
                event_type = "[META]" if event['is_meta'] else ""
                print(f"{i+1}. {event['time']} ticks: {event_type} {event['type']}")
                print(f"     详情: {event['details']}")
    else:
        print("读取MIDI文件失败")

if __name__ == "__main__":
    advanced_midi_analysis()
