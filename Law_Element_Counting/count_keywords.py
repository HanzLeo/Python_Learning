def count_keywords(file_path, keywords):
    """统计指定文件中关键词的出现次数"""
    keyword_counts = {keyword: 0 for keyword in keywords}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            for keyword in keywords:
                #不区分大小写，统计全词匹配（避免字符串误判）
                keyword_counts[keyword] += line.lower().count(keyword.lower())

    return keyword_counts

def save_report(report_path, counts):
    """将统计结果保存到文件"""
    with open(report_path,'w', encoding='utf-8') as report:
        report.write("关键词统计报告：\n")
        for keyword, count in counts.items():
            report.write(f"- {keyword}: {count}次\n")

# 使用示例
legal_file = "legal_document.txt"                         
keywords = ["合同","违约","赔偿"]
report_file = "keyword_report.txt"

counts = count_keywords(legal_file, keywords)
save_report(report_file, counts)

print(f"统计完成，报告已保存到{report_file}。")
