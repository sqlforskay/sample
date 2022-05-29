# coding=utf-8
template = {
'select_user_sql_by_type':'''
select * from sample where sample = "{sample}";
''',
'update_user_sql':'''
UPDATE sample SET sample="{sample}" WHERE sample="{sample}";
''',
'insere_sample_sql':'''
INSERT INTO user(sample,sample) values('{sample}','{sample}')  ON DUPLICATE KEY UPDATE sample='{sample}';
''',
'selece_sample_sql':'''
select * from sample limit {num1},{num2};
''',
'coune_sample_sql':'''
select count(*) from sample;
'''
}

python_template = {
'sample_select_sql':'''
select * from sample_table
''',
'sample_sql':'''
p_c.db.ExecNonQuery(s.t["sample_sql"].format(sample=p_c.db.secure(g_p_d['sample'])))
'''
}

t = template