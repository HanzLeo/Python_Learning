def count_keywords(file_path, keywords):
    """统计文本中关键词的出现次数"""
    keyword_counts = {keyword: 0 for keyword in keywords}  # 初始化计数字典
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.lower()
            for keyword in keywords:
                # 统计关键词在当前行的出现次数
                keyword_counts[keyword] += line.count(keyword.lower())
    return keyword_counts


# 实验样本
