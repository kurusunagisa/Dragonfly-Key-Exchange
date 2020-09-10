<<<<<<< HEAD
$ 
=======
#!/bin/sh

git filter-branch --env-filter '

OLD_EMAIL="tsubasa_sakaguchi0127@gmail.com"
CORRECT_NAME="soft-bear"
CORRECT_EMAIL="17411@g.nagano-nct.ac.jp"

if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
export GIT_COMMITTER_NAME="$CORRECT_NAME"
export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
export GIT_AUTHOR_NAME="$CORRECT_NAME"
export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags
>>>>>>> 4db266638ffb8620d3a08468a631f4bf8d18a0e3
