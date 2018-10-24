# This is a guide showing how to contribute to a Ayouto in very broad terms.
### Feel free to edit and improve this guide

* Clone the repository into your local machine
    ```
    git clone https://github.com/gunduzhuseyn/Tic-SPLE.git
    ```
* Before you begin to implement a new feature, make sure you are at the dev branch and it is up to date. 
    ```
    git checkout dev
    git pull origin dev
    ```
* To add new code, make sure to checkout a branch and work on that branch. Do not work on the dev branch directly!
    ```
    git checkout -b new-feature     #new-feature is the name of the new branch and should be descriptive
    ```
* After adding new code, and committing all the changes into this new branch, push it to the remote
    ```
    git push origin new-feature
    ```
* Finally create a merge request from new-branch to the dev branch.

**_Alternatively you can use your favorite IDE to handle checking out a new branch and pushing it to remote.
Common practices remain the same._**
