import numpy as np


class TreeNode(object):

    def __init__(self, prior_prob, parent=None):
        self.parent = parent
        self.children = {}  
        self.reward = 0  
        self.visited_times = 0
        self.prior_prob = prior_prob  
        
    def is_root(self):
        return self.parent is None

    def expand(self, action, probability):
        """
        Nếu như cái action đã có tức child node đã được expand thì trả về child node luôn còn k thì tạo child_node là 1 cái
        node mới rồi add nó vào dict
        """
        if action in self.children:
            return self.children[action]

        child_node = TreeNode(prior_prob=probability, parent = self)
        self.children[action] = child_node

        return child_node

    def UCT_function(self, c=5.0):
        greedy = c * self.prior_prob * np.sqrt(self.parent.visited_times) / (1 + self.visited_times)
        if self.visited_times == 0:
            return greedy
        return self.reward / self.visited_times + greedy

    def choose_best_child(self, c=5.0):
        """
        Kết quả trả ra sẽ giống như <(action(x_axis, y_axis), TreeNode)>, child_node[1] sẽ lấy ra TreeNode sau đó tính UCT_function(c) rồi mới trả ra kết quả max 
        """
        return max(self.children.items(), key=lambda child_node: child_node[1].UCT_function(c))

    def backpropagate(self, value):
        """
        Nó sẽ tự update reward và visited times của cái node này trước
        Sau đó check nó có phải root không, nếu k thì đệ quy lên parent
        Mỗi lần đệ quy lên nó sẽ là lượt chơi của người khác nhau nên phải thêm dấu trừ
        """
        self.visited_times += 1
        self.reward += value

        if not self.is_root():
            self.parent.backpropagate(-value)
