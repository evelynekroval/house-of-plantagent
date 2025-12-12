# Progress Tracker
## December 2025
### 12
- [x] Tool runs. Agent runs. That's great.
- [x] Issue is that they clearly don't pass information to each other. I _suspect_ the issue relates to context / runtime context, which I feel I've read about several times and I just don't grasp what the issue is.
- [ ] Okay, it does seem to work, but I'm noticing that it's best I restrict the websites it searches for so that I can control for these login popups which block the content. I've noticed that if I make the max_search = 2, it works better... **TODO:** Restrict websites Tavily searches from.
- [x] I still believe I need to understand the following better:
    - [x] Context
    - [x] RuntimeContext
    - [x] Tool Context?
- [x] Idle thought but, might it be helpful to include the LangChain guidance straight into Copilot as they advised?
- [ ] Added context & such - must really experiment with ResponseFormat in a sensible way so it doesn't duplicate what the tool returns... Does it need to go at the level of the tool? We shall see... **TODO:** Read about and toy with ResponseFormat
