#include <cmath>

class Solution {
public:
    /**
     * @param root the root of binary tree
     * @return the max node
     */
    TreeNode* maxNode(TreeNode *root) 
    {
        if (root == nullptr) {
            return nullptr;
        }
        
        auto curmax = root;
        
        maxNodeHelper(root, curmax);
        
        return curmax;
    }
    
private:
    void maxNodeHelper(TreeNode *root, TreeNode *&curmax)
    {
        if (root == nullptr) {
            return;
        }
        
        curmax = std::max(root, curmax, 
            [] (const TreeNode *left, const TreeNode *right) {
                return left->val < right->val;
            });
        
        maxNodeHelper(root->left,  curmax);
        maxNodeHelper(root->right, curmax);
    }
};
