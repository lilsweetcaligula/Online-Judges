/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 
 static int max(int a, int b);
 
 static int maxDepthHelper(const struct TreeNode *root, int depth);
 
int maxDepth(struct TreeNode* root) 
{
    return maxDepthHelper(root, 0);
}

static int maxDepthHelper(const struct TreeNode *root, int depth)
{
    if (root == NULL) {
        return depth;
    }
    
    return max(
        maxDepthHelper(root->left,  1 + depth),
        maxDepthHelper(root->right, 1 + depth)
    );
}

static int max(int a, int b)
{
    return (a > b) ? a : b;
}
