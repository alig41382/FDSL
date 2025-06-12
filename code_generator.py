class CodeGenerator:
    def __init__(self):
        pass
    #     self.operand_stack = []
    #     self.code_stack = []
    #     self.operators = ['+','-','*','/','=','<','>',
    #                       '==','<=','>=',
    #                       'begin_scope_operator',
    #                       'end_scope_operator'
    #                       ]
    #     self.key_counter = -1
    #     self.key_dict = {}
    #
    # def is_operator(self,item):
    #     return item in self.operators
    #
    # def create_key(self,id):
    #     self.key_counter = self.key_counter+1
    #     self.key_dict[id] = self.key_counter
    #     return self.key_counter
    #
    # def generate(self,traversal):
    #     for item in traversal:
    #         if self.is_operator(item):
    #             self.generate_code(item)
    #         else:
    #             self.operand_stack.append(item)
    #
    #     result = ""
    #     for code_piece in self.code_stack:
    #         result = result+ code_piece
    #     return result
    #
    # def generate_code(self, item):
    #     if item=='+':
    #         pass
    #     if item=='-':
    #         pass
    #     if item=='*':
    #         pass
    #     if item=='/':
    #         pass
    #     if item=='<':
    #         pass
    #     if item=='<=':    # we had div here
    #         pass
    #     if item=='>':
    #         pass
    #     if item=='>=':      # we had div here
    #         pass
    #     if item=='==':
    #         pass
    #     if item=='=':
    #         pass
    #     if item=='begin_scope_operator':
    #         self.code_stack.append('begin_scope_operator')
    #     if item=='end_scope_operator':
    #         self.code_stack.append('end_scope_operator')
