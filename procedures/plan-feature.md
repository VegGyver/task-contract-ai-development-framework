# Procedure — Plan a Feature or Change

Use planning when you have a feature, specification, analysis item, or desired
outcome that is too broad to implement as one bounded task.

1. Bind the existing project and provide the feature or available source material:

   ```txt
   tcaf plan --target <project-path> --request <feature-or-outcome>
   tcaf plan --target <project-path> --input <specification-or-analysis>
   ```

2. The planner reads the relevant current project and repository evidence. It
   works out practical dependencies, what is ready to do, and whether the
   requested work needs to be decomposed.
3. Review the proposed plan, task boundaries, dependencies, open decisions,
   and suggested next executable work. A dependency is semantic: it describes
   work that must be true first, not merely an item earlier in a list.
4. Approve, revise, or decline the proposal. Planning is reviewable preparation;
   it does not implement code, write Task Contracts, or change project state.
5. When a proposed task is ready, use `tcaf task` to generate its separate
   bounded Task Contract before implementation.

The plan is a developer-reviewed proposal. It does not replace decisions about
scope, acceptance, verification, or implementation approval.
