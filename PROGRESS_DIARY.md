# Progress Tracker
## December 2025
### 15
- [x] Reading about ResponseFormat, I realise it's 'structured' in the sense of a JSON or dictionary. It's not necessarily appropriate for what I need, and likely I can control this from system prompt. I've tried out an example and it works great.
- [x] Is it really necessary to restrict websites? Search tools can technically see past the usual limitations... 
- [x] On the bright side, adding it to the system prompt to only call the tool once per query seems to have solved it!
- [ ] I'm thinking about all the things I could be doing: implementing memory, mostly, or adding a UI. And all that matters to me is adding a UI... I've started doing that with the Agent UI provided by LangGraph, but the issue I'm having now is that I'm not passing 'user ID' apparently... The Agent UI chat is sort of using the code a little differently, apparently, so idk! **TODO**: Get a working response out of http://eu.smith.langchain.com/o/66bafab0-bdf5-4dd8-8219-4056ca6352b2/studio/thread?organizationId=66bafab0-bdf5-4dd8-8219-4056ca6352b2&render=trace&baseUrl=http%3A%2F%2F127.0.0.1%3A2024&threadId=c26e1f25-6969-494e-ae8f-7ad47c4e4545&mode=graph&assistantId=fe096781-5601-53d2-b2f6-0d3403f7e9ca&runtab=0. 
### 12
- [x] Tool runs. Agent runs. That's great.
- [x] Issue is that they clearly don't pass information to each other. I _suspect_ the issue relates to context / runtime context, which I feel I've read about several times and I just don't grasp what the issue is.
- [x] Okay, it does seem to work, but I'm noticing that it's best I restrict the websites it searches for so that I can control for these login popups which block the content. I've noticed that if I make the max_search = 2, it works better... **TODO:** Restrict websites Tavily searches from.
- [x] I still believe I need to understand the following better:
    - [x] Context
    - [x] RuntimeContext
    - [x] Tool Context?
- [x] Idle thought but, might it be helpful to include the LangChain guidance straight into Copilot as they advised?
- [x] Added context & such - must really experiment with ResponseFormat in a sensible way so it doesn't duplicate what the tool returns... Does it need to go at the level of the tool? We shall see... **TODO:** Read about and toy with ResponseFormat
