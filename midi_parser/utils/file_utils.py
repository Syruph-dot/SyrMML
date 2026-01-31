import os
import glob
from typing import List

class FileUtils:
    """
    文件工具类，用于处理MIDI相关的文件操作
    """
    
    @staticmethod
    def get_midi_files(directory: str, recursive: bool = False) -> List[str]:
        """
        获取目录中的MIDI文件列表
        
        Args:
            directory: 目录路径
            recursive: 是否递归搜索子目录
            
        Returns:
            List[str]: MIDI文件路径列表
        """
        pattern = os.path.join(directory, '**', '*.mid') if recursive else os.path.join(directory, '*.mid')
        return glob.glob(pattern, recursive=recursive)
    
    @staticmethod
    def get_mml_files(directory: str, recursive: bool = False) -> List[str]:
        """
        获取目录中的MML文件列表
        
        Args:
            directory: 目录路径
            recursive: 是否递归搜索子目录
            
        Returns:
            List[str]: MML文件路径列表
        """
        pattern = os.path.join(directory, '**', '*.mml') if recursive else os.path.join(directory, '*.mml')
        return glob.glob(pattern, recursive=recursive)
    
    @staticmethod
    def ensure_directory(directory: str):
        """
        确保目录存在，如果不存在则创建
        
        Args:
            directory: 目录路径
        """
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
    
    @staticmethod
    def get_filename_without_extension(file_path: str) -> str:
        """
        获取不带扩展名的文件名
        
        Args:
            file_path: 文件路径
            
        Returns:
            str: 不带扩展名的文件名
        """
        return os.path.splitext(os.path.basename(file_path))[0]
    
    @staticmethod
    def get_output_filename(input_file: str, output_dir: str, output_ext: str = '.mml') -> str:
        """
        生成输出文件名
        
        Args:
            input_file: 输入文件路径
            output_dir: 输出目录
            output_ext: 输出文件扩展名
            
        Returns:
            str: 输出文件路径
        """
        filename = FileUtils.get_filename_without_extension(input_file)
        return os.path.join(output_dir, f"{filename}{output_ext}")
    
    @staticmethod
    def read_file(file_path: str, encoding: str = 'utf-8') -> str:
        """
        读取文件内容
        
        Args:
            file_path: 文件路径
            encoding: 文件编码
            
        Returns:
            str: 文件内容
        """
        with open(file_path, 'r', encoding=encoding) as f:
            return f.read()
    
    @staticmethod
    def write_file(file_path: str, content: str, encoding: str = 'utf-8'):
        """
        写入文件内容
        
        Args:
            file_path: 文件路径
            content: 文件内容
            encoding: 文件编码
        """
        # 确保目录存在
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        
        with open(file_path, 'w', encoding=encoding) as f:
            f.write(content)
