from dataclasses import dataclass, field
from typing import List, Optional
import json


@dataclass
class legal_case:
    """法律案例的结构化数据类"""

    case_id: str
    title: str
    content: str
    keywords: list[str] = field(default_factory=list)
    category: Optional[str] = None  # 分类结果

    def to_dict(self) -> dict:
        return {
            "case_id": self.case_id,
            "title": self.title,
            "content": self.content,
            "keywords": self.keywords,
            "category": self.category,
        }


def classify_case(case: legal_case) -> None:
    """根据关键词自动分类案件类型"""
    match case.keywords:
        case ["合同", "违约", *rest]:
            case.category = "合同纠纷"
        case ["侵权", "赔偿", *rest]:
            case.category = "侵权责任"
        case ["劳动", "解雇", *rest]:
            case.category = "劳动争议"
        case _:
            case.category = "其他"


def save_to_json(cases: List[legal_case], file_path: str) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump([case.to_dict() for case in cases], f, ensure_ascii=False, indent=2)


# 示例数据
cases = [
    legal_case(
        case_id="C001",
        title="合同违约赔偿案",
        content="甲方未按合同条款履行义务，需赔偿乙方损失。",
        keywords=["合同", "违约", "赔偿"],
    ),
    legal_case(
        case_id="C002",
        title="员工解雇争议",
        content="公司单方面解雇员工，涉嫌违反劳动法。",
        keywords=["劳动", "解雇", "劳动法"],
    ),
]


# 分类并保存
for case in cases:
    classify_case(case)

save_to_json(cases, "legal_cases.json")

print("分类完成，结果已保存到 legal_cases.json")
