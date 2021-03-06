### How to Contribute

#### Please do not push to master.  

Major work should be done via pull requests (PR).  

##### This guide assumes you have already created a fork, and that you followed the "Quick Start" from the main README.md at the root of the repository.

#### 1. Create a topical branch

First, make sure your repository is up to date using:
```shell
$ git fetch upstream
```

Then, to merge it into your own project, type:
```shell
$ git merge upstream/master
```
Now you\'ll have an up-to-date version of the upstream code in your current branch.

To create a branch and switch to it use:
```shell
$ git checkout -b new-branch-name
```

To push your changes to your fork type:
```shell
$ git push origin new-branch-name
```

#### 2. Create a pull request

To create a PR, you must have changes committed to your new branch.
Go to the repository page on github and click on "Pull Request" button in the repo header.

Pick the branch you wish to have merged using the "Head branch" dropdown. You should leave the rest of the fields as is, unless you are working from a remote branch. In that case, just make sure that the base repo and base branch are set correctly.

Enter a title and description for your PR.  You can use markdown in the description.

Finally, click on the green "Send pull request" button to finish creating the pull request.

#### 3. Merging a pull request

Once you and your collaborators are happy with the changes, you start to merge the changes back to master.  There are a few ways to do this.

First, you can use github's "Merge pull request" button at the bottom of your pull request to merge your changes. This is only available when github can detect that there will be no merge conflicts with the base branch. If all goes well, you just have to add a commit message and click on "Confirm Merge" to merge the changes.

If the pull request cannot be merged online due to merge conflicts, or you wish to test things locally before sending the merge to the repo on Github, you can perform the merge locally instead.

#### 4. Closing a pull request

You can simply click on the "Close" button on the pull request to close it. Optionally, you can delete the branch directly using the "Delete this branch" button.
