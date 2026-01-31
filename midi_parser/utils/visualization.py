import matplotlib.pyplot as plt
from typing import List, Dict, Any

class MidiVisualizer:
    """
    MIDI可视化工具，用于将MIDI音符数据可视化
    """
    
    def visualize_notes(self, notes: List[Dict[str, Any]], output_path: str = None):
        """
        可视化音符序列
        
        Args:
            notes: 音符信息列表
            output_path: 输出文件路径（可选）
        """
        # 创建画布
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
        
        # 第一个子图：音符音高随时间变化
        self._plot_pitch_vs_time(ax1, notes)
        
        # 第二个子图：音符力度随时间变化
        self._plot_velocity_vs_time(ax2, notes)
        
        # 调整布局
        plt.tight_layout()
        
        # 保存或显示
        if output_path:
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            print(f"可视化图已保存到: {output_path}")
        else:
            plt.show()
        
        plt.close()
    
    def _plot_pitch_vs_time(self, ax, notes: List[Dict[str, Any]]):
        """
        绘制音符音高随时间变化的图表
        
        Args:
            ax: matplotlib轴对象
            notes: 音符信息列表
        """
        # 按音轨分组
        channels = set(note['channel'] for note in notes)
        
        for channel in channels:
            channel_notes = [note for note in notes if note['channel'] == channel]
            if not channel_notes:
                continue
            
            # 提取数据
            times = [note['start_time'] for note in channel_notes]
            pitches = [note['note'] for note in channel_notes]
            durations = [note['duration'] for note in channel_notes]
            
            # 绘制音符条
            ax.bar(times, heights=1, width=durations, bottom=pitches-0.5, 
                   align='edge', alpha=0.6, label=f'Channel {channel}')
        
        # 设置标签和标题
        ax.set_ylabel('音高 (MIDI音符数)')
        ax.set_title('音符音高随时间变化')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # 添加音高标签
        self._add_pitch_labels(ax)
    
    def _plot_velocity_vs_time(self, ax, notes: List[Dict[str, Any]]):
        """
        绘制音符力度随时间变化的图表
        
        Args:
            ax: matplotlib轴对象
            notes: 音符信息列表
        """
        # 按音轨分组
        channels = set(note['channel'] for note in notes)
        
        for channel in channels:
            channel_notes = [note for note in notes if note['channel'] == channel]
            if not channel_notes:
                continue
            
            # 提取数据
            times = [note['start_time'] for note in channel_notes]
            velocities = [note['velocity'] for note in channel_notes]
            
            # 绘制散点图
            ax.scatter(times, velocities, alpha=0.6, label=f'Channel {channel}')
        
        # 设置标签和标题
        ax.set_xlabel('时间 (ticks)')
        ax.set_ylabel('力度')
        ax.set_title('音符力度随时间变化')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 128)
    
    def _add_pitch_labels(self, ax):
        """
        在音高轴上添加音符名称标签
        
        Args:
            ax: matplotlib轴对象
        """
        # 获取当前y轴范围
        ymin, ymax = ax.get_ylim()
        
        # 生成音符名称标签（每12个半音一个八度）
        for note_num in range(int(ymin), int(ymax) + 1, 12):
            note_name = self._note_number_to_name(note_num)
            ax.text(-0.02, note_num, note_name, ha='right', va='center', 
                   transform=ax.get_yaxis_transform(), fontsize=8, color='gray')
    
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
    
    def visualize_mml_structure(self, mml: str, output_path: str = None):
        """
        可视化MML结构（简化版）
        
        Args:
            mml: MML字符串
            output_path: 输出文件路径（可选）
        """
        # 简单的MML结构可视化
        tokens = mml.split()
        
        # 创建画布
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # 绘制MML令牌流
        ax.plot(range(len(tokens)), [1] * len(tokens), 'o-', alpha=0.6)
        
        # 添加令牌标签
        for i, token in enumerate(tokens):
            ax.text(i, 1.1, token, ha='center', va='bottom', fontsize=8, rotation=45)
        
        # 设置标签和标题
        ax.set_xlabel('令牌索引')
        ax.set_title('MML结构可视化')
        ax.set_ylim(0.9, 1.2)
        ax.set_yticks([])
        ax.grid(True, alpha=0.3, axis='x')
        
        # 调整布局
        plt.tight_layout()
        
        # 保存或显示
        if output_path:
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            print(f"MML可视化图已保存到: {output_path}")
        else:
            plt.show()
        
        plt.close()
