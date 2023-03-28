/* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */


node * insert(node * root,int val)
{
int height(node *root)
{
    int l=-1,r=-1;
    if(root==NULL) return -1;
    if(root->left)l=root->left->ht;
    if(root->right)r=root->right->ht;
    return l>r?l+1:r+1;
}
node * right(node *n)
{
    node*old=n;
    node*lr=n->left->right;
    n=n->left;
    n->right=old;
    old->left=lr;
    old->ht=height(old);
    n->ht=height(n);
    return n;
}
node * left(node *n)
{
    node*old=n;
    node*rl=n->right->left;
    n=n->right;
    n->left=old;
    old->right=rl;
    old->ht=height(old);
    n->ht=height(n);
    return n;
}
int bal(node* root){
    
    int l=-1,r=-1;
    if(root==NULL) return -1;
    if(root->left)l=root->left->ht;
    if(root->right)r=root->right->ht;
    return l-r;
}
node * insert(node * root,int val)
{
	if(root==NULL){
        node *nn=new node();
        nn->val=val;
        nn->left=nn->right=NULL;
        nn->ht=0;
        return nn;
    }
    else if(root->val<val)root->right=insert(root->right,val);
    else root->left=insert(root->left,val);
    root->ht=height(root);
    if(bal(root)==2 and bal(root->left)==1){root=right(root);}
    if(bal(root)==-2 and bal(root->right)==-1){root=left(root);}
    if(bal(root)==2 and bal(root->left)==-1){root->left=left(root->left);root=right(root);}
    if(bal(root)==-2 and bal(root->right)==1){root->right=right(root->right);root=left(root);}
    return root;
}

}