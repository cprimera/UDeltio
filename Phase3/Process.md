## Phase 3: Kanban

*Column names:* TODO, Development, Testing, Merging

*Initial WIP*
Our initial WIP was 2 issues per team member (2 * 5) with the exception of TODO on which no limit was imposed. The reasons for this choice was that we have accounted for issues concerning bugs and a very likely hackathon before the deadline, where we would have to grab multiple issues. 

*Adjusted WIP*
The team decided to adjust initial WIP later in the Phase to match our workload speed. More specifically, we have discovered, that a team member tends to work on one issue at a time and switches to something else only if a really urgent fix is required, so we did not have an issue being stall in a particular column. We have decided that a more feasible limit to reflect this case would be number of team member + 1 per column. 
This could be adjusted a bit more with respect to Testing column, as it was mostly used either as an intermediate stage to make sure everything is working, or for bugfixes. However, the new limit is small enough by itself, and we plan to focus more on testing later, so we have decided to keep new limit for testing as well.

*GitHub Issues Conventions:*
- Kanban columns (except for TODO) had corresponding labels on GitHub. TODO was implicit and consisted of open issues assigned to Phase3 that did not enter Development.
- Branches naming conventions:
- - feature/branchName for features
- - bug/branchName for bugs
- WIP limits were enforced with pure observation and calculation. That is, if there are 10 issues labeled with ‘Development’, no new issues can be grabbed.
- Closing the issues by commit messages: since we were using GitFlow, did not work: all issues would be closed only on merging `develop` branch into `master`, which is done in the end of the phase. Instead, we have used commit messages to have the issue reference respective pull request. 

*Kanban versus the Scrum-like process*
Overall, we like Kanban better. Labels on GitHub issues are quite specific about the progress on the issue, so the timeline could be planned much better. We also think that the WIP has helped us to stay more organized and not to grab more issues than one wanted, which is why we did not have stale issues. 
One thing that we seemed to carry from Scrum-like process to this phase was that if a team member grabs a task and the task is stale for a couple of days, another team member will remove the assignee and grab it following the progress that was made.
Another thing that we liked about Kanban was much less documentation that had to be created in the middle of the phase. This has allowed us to focus more on code and thus we were able to complete more issues by far, comparing to previous phase. 
The only drawback of Kanban for our team was that we did not have frontend testing set up, so a much more efficient setup for a frontend would be to have just two columns (Development and Merging). However, we felt like Testing was necessary at least for bugfixes, but, since those are short, issues usually stayed in it for at most ten minutes, and we think we should have been allowed to skip columns instead of assigning labels to Testing back and forth to follow the process. 
