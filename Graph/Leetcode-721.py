from typing import List
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size+1))
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # 路径压缩
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u  # 合并

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_id = {}
        email_to_name = {}
        union_find = UnionFind(10000)  # 可以调整大小
        current_id = 0
        
        # Step 1: 遍历账户并构建邮箱和ID的映射，合并邮箱
        for account in accounts:
            name = account[0]
            #first_email = account[1]  # 第一个邮箱用作“根”节点
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = current_id
                    current_id += 1
                email_to_name[email] = name
                union_find.union(email_to_id[account[1]], email_to_id[email])  # 将当前邮箱与第一个邮箱合并
                
        # Step 2: 将具有相同根的邮箱合并到一起
        id_to_emails = {}
        for email in email_to_id:
            root_id = union_find.find(email_to_id[email])
            if root_id not in id_to_emails:
                id_to_emails[root_id] = []
            id_to_emails[root_id].append(email)
        
        # Step 3: 构造最终结果
        result = []
        for emails in id_to_emails.values():
            emails.sort()  # 按字典序排序
            result.append([email_to_name[emails[0]]] + emails)  # 第一个邮箱映射到用户名
        return result