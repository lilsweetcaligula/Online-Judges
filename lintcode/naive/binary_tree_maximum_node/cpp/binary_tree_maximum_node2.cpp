#include <cmath>
#include <stack>

class Solution {
public:
    /**
     * @param root the root of binary tree
     * @return the max node
     */
    TreeNode* maxNode(TreeNode* root) 
    {
        if (root == nullptr) {
            return nullptr;
        }
        
        auto stack  = std::stack<TreeNode*>{ };
        auto curmax = root;
        
        stack.push(root);
        
        while (stack.size() > 0) 
        {
            const auto node = stack.top();
            
            curmax = std::max(node, curmax,
                [] (const TreeNode *left, const TreeNode *right) {
                    return left->val < right->val;
                });
            
            stack.pop();
            
            if (node->left != nullptr) {
                stack.push(node->left);
            }
            
            if (node->right != nullptr) {
                stack.push(node->right);
            }
        }
        
        return curmax;
    }
};
