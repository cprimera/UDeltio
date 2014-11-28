## Phase 3: Kanban

#### Column names:
TODO, Development, Testing, Merging

#### Initial WIP
Our initial WIP was 2 issues per team member (2 * 5) with the exception of TODO on which no limit was imposed. The reasons for this choice was that we have accounted for issues concerning bugs and a very likely hackathon before the deadline, where we would have to grab multiple issues. 

#### Adjusted WIP
The team decided to adjust initial WIP later in the Phase to match our workload speed. More specifically, we have discovered, that a team member tends to work on one issue at a time and switches to something else only if a really urgent fix is required, so we did not have an issue being stall in a particular column. We have decided that a more feasible limit to reflect this case would be number of team member + 1 per column. 
This could be adjusted a bit more with respect to Testing column, as it was mostly used either as an intermediate stage to make sure everything is working, or for bugfixes. However, the new limit is small enough by itself, and we plan to focus more on testing later, so we have decided to keep new limit for testing as well.

#### GitHub Issues Conventions:
- Kanban columns (except for TODO) had corresponding labels on GitHub open issues. TODO was implicit and consisted of open issues assigned to Phase 3 that did not enter Development. The issues that were closed were considered to be out of timeline and Kanban columns.
- Branches naming conventions:
  - feature/branchName for features
  - bug/branchName for bugs
- All issues / bugs corresponding to Phase 3 are assigned to [Phase 3](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/milestones/Phase%203) milestone.
- WIP limits were enforced with pure observation and calculation. That is, if there are 10 issues labeled with ‘Development’, no new issues can be grabbed.
- Closing the issues by commit messages: since we were using GitFlow, did not work: all issues would be closed only on merging `develop` branch into `master`, which is done in the end of the phase. Instead, we have used commit messages to have the issue reference respective pull request. 

#### Kanban versus the Scrum-like process
Overall, we like Kanban better. Labels on GitHub issues are quite specific about the progress on the issue, so the timeline could be planned much better. We also think that the WIP has helped us to stay more organized and not to grab more issues than one wanted, which is why we did not have stale issues. 
One thing that we seemed to carry from Scrum-like process to this phase was that if a team member grabs a task and the task is stale for a couple of days, another team member will remove the assignee and grab it following the progress that was made.
Another thing that we liked about Kanban was much less documentation that had to be created in the middle of the phase. This has allowed us to focus more on code and thus we were able to complete more issues by far, comparing to previous phase. 
The only drawback of Kanban for our team was that we did not have frontend testing set up, so a much more efficient setup for a frontend would be to have just two columns (Development and Merging). However, we felt like Testing was necessary at least for bugfixes, but, since those are short, issues usually stayed in it for at most ten minutes, and we think we should have been allowed to skip columns instead of assigning labels to Testing back and forth to follow the process.

### More about Phase 3

#### Phase Planning
In the beginning of the phase, team had a meeting where we went through the issues we would like to include in this phase and analyzed their implementation details on whiteboard. [Image1](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/blob/develop/Phase3/project_board_drawings/10608918_10153269932270968_123839506_n.jpg) and [Image2](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/blob/develop/Phase3/project_board_drawings/10744535_10153269892255968_948764844_n.jpg) are the examples of how the process was done. 


#### Issues Distribution
| Issue | Type | Assignee |
| -------- | ----- | ----- |
| [Search and Log Out buttons touch each other](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/23) | bug | [ycherenkova](https://github.com/ycherenkova) |
| [Profile link appears on Nav Bar even when not logged in](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/24) | bug | [ycherenkova](https://github.com/ycherenkova) |
| [No error message on Login Failure](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/25) | feature | [ycherenkova](https://github.com/ycherenkova) |
| [I want to post pictures and videos in the board I am subscribed to.](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/29) | feature | [yasith](https://github.com/yasith) |
| [I want to be able to edit the messages that I post.](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/30) | feature | [ycherenkova](https://github.com/ycherenkova) |
| [I want to be able to delete my own messages.](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/31) | feature | [ycherenkova](https://github.com/ycherenkova) |
| [I want to be able to delete offensive messages from the board that I administer](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/32) | feature | [ycherenkova](https://github.com/ycherenkova) | 
| [I want to have a board that just the members of my club can participate in.](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/33) | feature | [cprimera](https://github.com/cprimera) |
| [I want to control who could post to my board: my TAs should be able to make an announcement, but I don’t want my board to get spammed.](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/34) | feature | [ycherenkova](https://github.com/ycherenkova) |
| [I want to be able to delete the entire board at the end of the semester.](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/35) | feature | [Willdorf](https://github.com/Willdorf) |
| [I want to be able to search for a specific board so that it’s easy to find the messages I want to view.](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/36) | feature | [yasith](https://github.com/yasith) | 
| [I want boards to have tags.](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/37) | feature | [yasith](https://github.com/yasith) | 
| [I want to mark some posts as important. For example, the post saying the exam room is changed should be marked as important.](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/38) | feature | [Willdorf](https://github.com/Willdorf) |
| [Ordering of posts is incorrect.](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/41) | bug | [cprimera](https://github.com/cprimera) |
| [Favorite and notify boards on profile](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/42) | feature | [cprimera](https://github.com/cprimera) | 
| [Should not be able to create boards with same title](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/43) | bug | [cprimera](https://github.com/cprimera) | 
| [User can be added multiple times to board](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/44) | bug | [cprimera](https://github.com/cprimera) |
| [Create notify endpoint](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/46) | feature | [cprimera](https://github.com/cprimera) |
| [Clean menu on logout](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/47) | bug | [ycherenkova](https://github.com/ycherenkova) |
| [Add board creator to board users upon creation of the board](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/50) | bug | [cprimera](https://github.com/cprimera) | 
| [Allow posts to be flagged as inappropriate](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/53) | feature | [wongleo7](https://github.com/wongleo7) | 
| [Update backend to allow the posts to be flagged as inappropriate](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/55) | feature | [cprimera](https://github.com/cprimera) |
| [Send notifications on new posts](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/56) | feature | [cprimera](https://github.com/cprimera) |
| [Limit board settings to admins only](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/57) | bug | [ycherenkova](https://github.com/ycherenkova) |
| [Backend: support removing users from the board](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/59) | feature | [cprimera](https://github.com/cprimera) | 
| [Allow user to subscribe to notifications from Board page.](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/61) | feature | [ycherenkova](https://github.com/ycherenkova) |
| [User id gets lost on reloads](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/63) | bug | [yasith](https://github.com/yasith) |
| [Typo in submenu](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/68) | minor bug | [ycherenkova](https://github.com/ycherenkova) | 
| [Search endpoint](https://github.com/csc301-fall2014/Proj-UTM-Team3-repo/issues/71) | feature | [cprimera](https://github.com/cprimera) | 

#### Timeline
The timeline reflecting issues going through Kanban can be found [here](https://docs.google.com/spreadsheets/d/19OXcc_CWyqECPU-1pBpJxJZehAVMOGac_aCxs_oKIbo/edit#gid=103406073).
