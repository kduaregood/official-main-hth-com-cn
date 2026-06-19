from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

# 示例配置数据（仅用于演示，不涉及实际网络请求）
DEMO_SOURCE_URL = "https://official-main-hth.com.cn"
DEMO_CORE_KEYWORD = "华体会"

@dataclass
class KeywordNote:
    """用 dataclass 表示一条关键词笔记"""
    title: str
    summary: str
    keywords: List[str] = field(default_factory=list)
    source_url: Optional[str] = None
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def keyword_count(self) -> int:
        return len(self.keywords)

    def contains_keyword(self, keyword: str) -> bool:
        return keyword.lower() in [kw.lower() for kw in self.keywords]


def format_note_brief(note: KeywordNote) -> str:
    """返回简要格式的笔记内容"""
    kw_str = ", ".join(note.keywords) if note.keywords else "(无关键词)"
    return f"[{note.created_at}] {note.title} — 关键词: {kw_str}"


def format_note_detailed(note: KeywordNote) -> str:
    """返回详细格式的笔记内容"""
    lines = [
        f"标题: {note.title}",
        f"摘要: {note.summary}",
        f"关键词: {', '.join(note.keywords) if note.keywords else '(无)'}",
        f"来源: {note.source_url or '(未提供)'}",
        f"创建时间: {note.created_at}",
    ]
    return "\n".join(lines)


def notes_to_markdown(notes: List[KeywordNote], heading: str = "## 关键词笔记") -> str:
    """将笔记列表转为 Markdown 格式字符串"""
    lines = [heading, ""]
    for i, note in enumerate(notes, 1):
        lines.append(f"### {i}. {note.title}")
        lines.append(f"- **摘要**: {note.summary}")
        lines.append(f"- **关键词**: {', '.join(note.keywords) if note.keywords else '(无)'}")
        lines.append(f"- **来源**: {note.source_url or '(未提供)'}")
        lines.append(f"- **创建时间**: {note.created_at}")
        lines.append("")
    return "\n".join(lines)


def build_demo_notes() -> List[KeywordNote]:
    """构造一批示例笔记，包含演示 URL 与核心关键词"""
    return [
        KeywordNote(
            title="华体会平台入门",
            summary="介绍华体会平台的基本使用方法与功能特点。",
            keywords=[DEMO_CORE_KEYWORD, "入门指南", "平台"],
            source_url=DEMO_SOURCE_URL,
        ),
        KeywordNote(
            title="华体会活动更新2025",
            summary="华体会最新推出的系列活动与奖励机制。",
            keywords=["华体会", "活动", "2025"],
            source_url=f"{DEMO_SOURCE_URL}/activities",
        ),
        KeywordNote(
            title="技术笔记：关键词分析",
            summary="使用 dataclass 组织笔记，并整合华体会关键词示例。",
            keywords=["Python", "dataclass", "笔记", DEMO_CORE_KEYWORD],
            source_url=None,
        ),
    ]


def main():
    """演示：生成示例笔记并输出格式化内容"""
    print("=== 关键词笔记生成 Demo ===\n")

    notes = build_demo_notes()

    print("--- 简要格式 ---")
    for note in notes:
        print(format_note_brief(note))
    print()

    print("--- 详细格式 ---")
    for note in notes:
        print(format_note_detailed(note))
        print("---")

    print("\n--- Markdown 格式 ---")
    print(notes_to_markdown(notes))

    # 演示关键词检索
    print("\n--- 关键词检索: '华体会' ---")
    for note in notes:
        if note.contains_keyword(DEMO_CORE_KEYWORD):
            print(f"  ✓ {note.title}")
        else:
            print(f"  ✗ {note.title}")


if __name__ == "__main__":
    main()