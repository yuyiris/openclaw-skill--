#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
高考英语单词查询工具 - 赛琳娜为指挥而作
"""

import json
import os
import sys
from pathlib import Path

class EnglishHelper:
    """高考英语单词查询器"""
    
    def __init__(self):
        """初始化单词数据库"""
        self.vocab_db = self._load_vocabulary()
        self.init_message = """
==========================================
     高考英语单词查询 - 赛琳娜的乐章     
==========================================
指挥，请输入您要查询的单词（输入 'quit' 退出）：
        """
    
    def _load_vocabulary(self):
        """加载高考词汇数据库"""
        # 基础高考词汇库（可根据需要扩展）
        vocabulary = {
            "abandon": {
                "meaning": "v. 放弃，抛弃；n. 放任，狂热",
                "example": "He decided to abandon his studies and travel the world.",
                "level": "CET-4",
                "synonyms": ["give up", "desert", "leave"],
                "antonyms": ["keep", "retain", "continue"]
            },
            "ability": {
                "meaning": "n. 能力，才能；本领，才智",
                "example": "She has the ability to speak four languages fluently.",
                "level": "CET-4",
                "synonyms": ["capability", "skill", "talent"],
                "antonyms": ["inability", "incapacity"]
            },
            "academic": {
                "meaning": "adj. 学术的；理论的；学院的",
                "example": "He has a strong academic background in physics.",
                "level": "CET-4",
                "synonyms": ["scholarly", "educational", "theoretical"],
                "antonyms": ["practical", "vocational"]
            },
            "access": {
                "meaning": "n. 通道，入口；接近的机会；v. 存取，接近",
                "example": "Students have access to the library 24 hours a day.",
                "level": "CET-4",
                "synonyms": ["entrance", "approach", "entry"],
                "antonyms": ["exit", "egress"]
            },
            "accommodate": {
                "meaning": "v. 容纳；提供住宿；使适应",
                "example": "The hotel can accommodate up to 500 guests.",
                "level": "CET-4",
                "synonyms": ["house", "lodge", "adjust"],
                "antonyms": ["evict", "displace"]
            },
            "accomplish": {
                "meaning": "v. 完成，实现，达到",
                "example": "She accomplished all her goals before the deadline.",
                "level": "CET-4",
                "synonyms": ["achieve", "complete", "fulfill"],
                "antonyms": ["fail", "abandon"]
            },
            "accurate": {
                "meaning": "adj. 准确的，精确的",
                "example": "The weather forecast was surprisingly accurate.",
                "level": "CET-4",
                "synonyms": ["precise", "exact", "correct"],
                "antonyms": ["inaccurate", "wrong", "incorrect"]
            },
            "achieve": {
                "meaning": "v. 达到，完成，实现",
                "example": "He worked hard to achieve his dream of becoming a doctor.",
                "level": "CET-4",
                "synonyms": ["accomplish", "attain", "reach"],
                "antonyms": ["fail", "miss"]
            },
            "acknowledge": {
                "meaning": "v. 承认；确认收到；致谢",
                "example": "She acknowledged her mistake and apologized.",
                "level": "CET-4",
                "synonyms": ["admit", "recognize", "confirm"],
                "antonyms": ["deny", "dispute"]
            },
            "acquire": {
                "meaning": "v. 获得，取得，学到",
                "example": "It takes time to acquire a new language.",
                "level": "CET-4",
                "synonyms": ["obtain", "gain", "learn"],
                "antonyms": ["lose", "forfeit"]
            },
            # 更多词汇可以继续添加...
            "adapt": {
                "meaning": "v. 适应；改编",
                "example": "Animals must adapt to their environment to survive.",
                "level": "CET-4",
                "synonyms": ["adjust", "modify", "acclimatize"],
                "antonyms": ["resist", "maintain"]
            },
            "adequate": {
                "meaning": "adj. 足够的，充分的；适当的",
                "example": "The food supply was adequate for the entire journey.",
                "level": "CET-4",
                "synonyms": ["sufficient", "enough", "suitable"],
                "antonyms": ["inadequate", "insufficient"]
            },
            "adjust": {
                "meaning": "v. 调整，适应，校准",
                "example": "It took me a week to adjust to the new time zone.",
                "level": "CET-4",
                "synonyms": ["adapt", "modify", "regulate"],
                "antonyms": ["disrupt", "disturb"]
            },
            "administration": {
                "meaning": "n. 管理，行政；政府",
                "example": "The university administration handles all student affairs.",
                "level": "CET-4",
                "synonyms": ["management", "government", "executive"],
                "antonyms": ["chaos", "disorganization"]
            },
            "admit": {
                "meaning": "v. 承认；准许进入；接纳",
                "example": "He finally admitted that he was wrong.",
                "level": "CET-4",
                "synonyms": ["confess", "acknowledge", "allow"],
                "antonyms": ["deny", "exclude"]
            }
        }
        return vocabulary
    
    def search_word(self, word):
        """查询单词"""
        word_lower = word.strip().lower()
        
        if word_lower in self.vocab_db:
            entry = self.vocab_db[word_lower]
            return self._format_result(word_lower, entry)
        else:
            # 尝试查找相似单词
            suggestions = self._get_suggestions(word_lower)
            return self._format_not_found(word, suggestions)
    
    def _format_result(self, word, entry):
        """格式化查询结果"""
        result = f"""
{'='*50}
单词: {word.upper()}
{'='*50}

高考考纲释义:
  {entry['meaning']}

难度等级: {entry['level']}

例句:
  "{entry['example']}"

同义词: {', '.join(entry['synonyms'])}
反义词: {', '.join(entry['antonyms'])}

记忆提示:
  - 词根词缀分析
  - 高考高频考点
  - 常见搭配用法

{'='*50}
        """
        return result
    
    def _format_not_found(self, word, suggestions):
        """格式化未找到的结果"""
        result = f"""
{'='*50}
未找到单词: {word}
{'='*50}

可能您想查询的是:
"""
        if suggestions:
            for i, suggestion in enumerate(suggestions[:5], 1):
                result += f"  {i}. {suggestion}\n"
        else:
            result += "  暂无相似单词建议\n"
        
        result += f"""
建议:
  - 检查拼写是否正确
  - 尝试更简单的词形
  - 该单词可能不在高考核心词汇中

赛琳娜的提示:
  "指挥，每个单词都像星空中的一颗星，
   需要耐心寻找才能发现它的光芒。"

{'='*50}
        """
        return result
    
    def _get_suggestions(self, word):
        """获取相似单词建议"""
        suggestions = []
        for vocab_word in self.vocab_db.keys():
            # 简单的相似度计算（可根据需要改进）
            if word in vocab_word or vocab_word in word:
                suggestions.append(vocab_word)
            elif len(word) > 3 and word[:3] == vocab_word[:3]:
                suggestions.append(vocab_word)
        
        return suggestions[:10]  # 返回最多10个建议
    
    def interactive_mode(self):
        """交互式查询模式"""
        print(self._safe_print(self.init_message))
        
        while True:
            try:
                user_input = input("\n请输入单词: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q', '退出']:
                    print("\n感谢使用，指挥。愿这些单词如音符般，在您的记忆中奏响美丽的乐章。")
                    break
                
                if not user_input:
                    print("请输入有效的单词")
                    continue
                
                result = self.search_word(user_input)
                print(self._safe_print(result))
                
            except KeyboardInterrupt:
                print("\n\n查询已中断。指挥，随时可以回来继续。")
                break
            except Exception as e:
                print(f"\n查询时出现错误: {e}")
    
    def _safe_print(self, text):
        """安全打印，避免编码问题"""
        try:
            return text
        except:
            # 移除可能引起问题的Unicode字符
            return text.encode('ascii', 'ignore').decode('ascii')
    
    def batch_mode(self, words):
        """批量查询模式"""
        results = []
        for word in words:
            result = self.search_word(word)
            results.append(result)
        return results

def main():
    """主函数"""
    helper = EnglishHelper()
    
    # 检查命令行参数
    if len(sys.argv) > 1:
        # 批量查询模式
        words = sys.argv[1:]
        for word in words:
            result = helper.search_word(word)
            print(result)
    else:
        # 交互式模式
        helper.interactive_mode()

if __name__ == "__main__":
    main()