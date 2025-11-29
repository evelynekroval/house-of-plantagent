
# TODO: house-of-plantagent

## Phase 1: Project Foundation & Discovery
- [ ] **Initialize Python project structure**
    -  [x] Create `pyproject.toml` (or `requirements.txt`) with base dependencies
    -  [x] Set up virtual environment: `python -m venv venv`
    -  [ ] Add dev tools: `pytest`, `black`, `ruff` for linting/formatting
    - *Why:* Ensures reproducible builds and follows Python conventions

- [ ] **Create README.md with vision & architecture**
    - [x] Link to `copilot-instructions.md`
    - [ ] Diagram: User → Agent → Retrieval → Grounding → Recipe Output
    - *Why:* Helps reviewers and future contributors understand scope

- [ ] **Decide on orchestration framework**
    - [ ] Options: **LangChain** (popular, good docs), **LlamaIndex** (RAG-focused), **custom loop** (simplest)
    - [ ] Recommend: Start with **custom agentic loop** to avoid "black box" hallucinations
    - *Why:* Aligns with "every component inspectable" principle

---

## Phase 2: Data & Grounding Layer
- [ ] **Identify recipe data sources**
    - [ ] Research open recipe APIs/datasets: `RecipeNLG`, `Spoonacular` (free tier), or web scraping
    - [ ] Document licensing & attribution rules
    - *Why:* "Recipes retrieved from real sources, never hallucinated"

- [ ] **Build retrieval pipeline**
    - [ ] Choose vector DB: **Chroma** or **FAISS** (both local, open-source)
    - [ ] Or simpler: keyword search + BM25 ranking
    - [ ] Implement: `RecipeStore` class with `search(query, filters)` method
    - *Why:* Enables user preference filtering (ingredients, cuisines, dislikes)

- [ ] **Set up nutritional grounding**
    - [ ] Find open nutrition data: **USDA FoodData Central**, **OpenFoodFacts** API
    - [ ] Build scraper/enricher: `NutritionFacts` class mapping ingredients → macros/micros
    - [ ] Store in lightweight DB (SQLite or JSON)
    - *Why:* Prevents nutritional claims from being invented

---

## Phase 3: Agent Logic
- [ ] **Define agent state & tools**
    - [ ] State schema: `{ user_query, preferences, retrieved_recipes, grounding_checks, final_recommendation }`
    - [ ] Tools: `retrieve_recipes()`, `check_nutrition()`, `filter_by_preference()`, `rank_recipes()`
    - *Why:* Makes decision flow explicit and testable

- [ ] **Implement agentic loop**
    - [ ] Pseudocode:
        ```
        while not user_satisfied:
            1. Parse user input → extract preferences
            2. Retrieve candidates
            3. Ground each: check nutrition, ingredient availability
            4. Rank & explain reasoning
            5. Ask user for refinement
        ```
    - *Why:* Demonstrates orchestration without magic

- [ ] **Add explainability**
    - [ ] Log every retrieval, filtering, and grounding decision
    - [ ] Return reasoning alongside recommendations: `"Why: high protein, low sodium, matches your vegan nut allergy"`
    - *Why:* Evaluable & auditable

---

## Phase 4: Testing & Evaluation
- [ ] **Unit tests for each component**
    - [ ] Test `RecipeStore.search()`, `NutritionFacts.calculate_macros()`, filtering logic
    - [ ] Use `pytest`; create `tests/` directory
    - *Why:* Catches hallucinations and regressions early

- [ ] **Integration tests for agent loop**
    - [ ] Mock user queries: "high-protein, no nuts, quick weeknight dinners"
    - [ ] Assert: recommendations are real (from data), reasoning is logged, no invented facts
    - *Why:* Validates end-to-end grounding

- [ ] **Evaluation rubric**
    - [ ] Hallucination rate: 0% (all claims traceable to sources)
    - [ ] Retrieval precision: recipes match user preferences
    - [ ] Reasoning clarity: user can explain "why this recipe"

---

## Phase 5: MVP & Documentation
- [ ] **CLI or simple interface**
    - [ ] Minimal: `python -m house_of_plantagent --query "..." --preferences "..."`
    - [ ] Or: Jupyter notebook demo with step-by-step walkthrough
    - *Why:* Makes it usable & shareable

- [ ] **Document design decisions**
    - [ ] Why retrieval over generation? 
    - [ ] Why that vector DB? 
    - [ ] Why that grounding approach?
    - [ ] Add to `docs/` or inline in code comments
    - *Why:* Explains trade-offs; helps reviewers validate approach

---

## Suggested Libraries (Open-Source, Zero-Cost)
| Component | Library | Why |
|-----------|---------|-----|
| **Orchestration** | Custom loop + `dataclasses` | Transparent, no hidden magic |
| **Retrieval** | `FAISS` or `Chroma` | Local vector search; no external calls |
| **LLM** | `Ollama` (local) or `llama.cpp` | Privacy, no API costs |
| **Data** | `pandas`, SQLite | Lightweight, familiar |
| **Testing** | `pytest` | Standard in Python |
| **Linting** | `ruff`, `black` | Fast, no config hell |

---

## Next Steps
1. Create `pyproject.toml` with minimal deps (e.g., `faiss-cpu`, `pandas`, `pytest`)
2. Pick one data source (e.g., scrape a public recipe site or use an API)
3. Build `RecipeStore` class with search; write 5 unit tests
4. Share code → iterate on design feedback

*Update this TODO as you discover the actual tech stack and add concrete examples.*
