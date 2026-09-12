from mpmath import mp

# ===================== 配置 =====================
# 小数点后精度：100万位
mp.dps = 1000000
# 保存路径（正斜杠写法，Windows 完全兼容，避免转义报错）
save_path = "D:/学习文件/GitHub/python-practice/read_file/pi_digits.txt"
# ===============================================

# 生成 π 的完整字符串
pi_str = str(mp.pi)
integer_part, decimal_part = pi_str.split('.')
# 严格截取前 100 万位小数，避免精度冗余
decimal_part = decimal_part[:1000000]

with open(save_path, 'w', encoding='utf-8') as f:
    # 第一行：3. + 前10位小数（和你截图格式一致）
    f.write(f"{integer_part}.{decimal_part[:10]}\n")
    
    # 剩余小数部分：每10位一行写入
    rest = decimal_part[10:]
    for i in range(0, len(rest), 10):
        f.write(rest[i:i+10] + '\n')

print(f"✅ 生成完成！文件已保存到：{save_path}")
