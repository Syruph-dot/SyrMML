#!/usr/bin/env python3
"""
MIDI到MML转换示例
展示如何使用MMLConverter将MIDI文件转换为MML格式
"""

from midi_parser import MMLConverter, MidiReader, FileUtils

def midi_to_mml_conversion():
    """MIDI到MML转换示例"""
    # 输入和输出文件路径
    input_file = "example.mid"  # 这里需要替换为实际的MIDI文件路径
    output_dir = "output"
    
    # 确保输出目录存在
    FileUtils.ensure_directory(output_dir)
    
    # 创建MMLConverter实例
    converter = MMLConverter()
    
    # 转换文件
    output_file = FileUtils.get_output_filename(input_file, output_dir, ".mml")
    if converter.convert_file(input_file, output_file):
        print(f"MIDI文件转换成功!")
        print(f"输入文件: {input_file}")
        print(f"输出文件: {output_file}")
        
        # 读取并显示生成的MML
        mml_content = FileUtils.read_file(output_file)
        print(f"\n=== 生成的MML内容 ===")
        print(mml_content)
    else:
        print(f"MIDI文件转换失败!")

if __name__ == "__main__":
    midi_to_mml_conversion()
