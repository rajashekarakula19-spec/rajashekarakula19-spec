# Hi, I'm Rajashekar Akula

**Software Engineering · Applied AI · Machine Learning**

I build applications that turn data into useful decisions—combining machine learning, AI assistants, backend APIs, and interactive web interfaces.

My current projects span retail inventory, energy demand, hospital operations, and personalized restaurant discovery. Across these domains, I focus on connecting a model's output to a clear, usable product experience.

## My story

I approach software through practical questions. Can a retailer spot stockout risk early enough to investigate? Can an energy dashboard explain yesterday's costs and forecast tomorrow's demand? Can hospital comparisons account for differences in the patients they serve?

These questions shape how I work across the stack—from preparing data and evaluating models to building APIs and designing the interface where someone explores the results. My projects combine Python-based analytics and machine learning with web development in TypeScript and React.

I'm also bringing generative AI into these workflows. In ShelfSignal, a retrieval-grounded assistant explains project evidence with citations. In FooLover, optional local language-model interpretation connects natural-language requests to restaurant discovery. These projects let me explore how predictive models, language models, and application logic can work together.

My engineering priorities are clear evaluation, traceable answers, and honest communication of what a system can support. I want someone exploring my work to understand both how it was built and why its results matter.

## Featured projects

### [ShelfSignal — Retail Stockout Early Warning](https://github.com/rajashekarakula19-spec/retail-stockout-early-warning)

A retail analytics application that predicts seven-day stockout risk and presents alerts, likely risk drivers, and suggested inventory actions. Its evaluation uses chronological splits, a frozen alert threshold, baseline comparisons, and measures of false-alert workload and useful warning time.

Its local RAG assistant retrieves versioned project evidence, validates citations, and abstains when evidence is insufficient. The public dashboard provides a static demonstration; full RAG generation requires the backend and Ollama. Reported historical losses are retrospective estimates, not demonstrated savings.

**Focus:** Predictive ML · Retrieval-augmented generation · Grounded explanations · Evaluation  
**Stack:** Python, XGBoost, PostgreSQL, FastAPI, React, Ollama

### [Voltart — Industrial Energy Analytics & Demand Forecasting](https://github.com/rajashekarakula19-spec/industrial-energy-analytics-and-electricity-demand-forecasting)

An energy analytics portfolio application connecting cost analysis with a 14-day electricity demand forecast. It combines budget-versus-actual views, cost breakdowns, gradient-boosting forecasts, and actual-versus-predicted backtests using synthetic industrial data.

**Focus:** Time-series forecasting · Data pipelines · Model backtesting · Interactive analytics  
**Stack:** Python, scikit-learn, pandas, FastAPI, Next.js, TypeScript

### [Finger Lakes — Inpatient Planning & Opportunity Dashboard](https://github.com/rajashekarakula19-spec/los-pjt)

A hospital operations research prototype using 2024 New York SPARCS data to compare length of stay and cost against case-mix-adjusted expectations. Out-of-fold modeling, uncertainty intervals, and false-discovery-rate controls help prioritize patterns for human investigation.

**Focus:** Applied ML · Statistical evaluation · Interpretable analytics · Healthcare operations research  
**Stack:** Python, scikit-learn, FastAPI, HTML, CSS, JavaScript

### [FooLover — AI-Assisted Restaurant Discovery & Meal Planning](https://github.com/rajashekarakula19-spec/Foolover)

A Buffalo-focused product demo connecting restaurant discovery, meal selection, cost estimates, and an itinerary. It combines optional local LLM interpretation with recommendation ranking, map-based search, and heuristic fallbacks. Menus, prices, and wait estimates include demo data.

**Focus:** Local LLM integration · Personalized recommendations · Full-stack product development  
**Stack:** React, TypeScript, FastAPI, Ollama, MapLibre, PostgreSQL/PostGIS

## Technical toolkit

| Area | Technologies and methods used across my projects |
| --- | --- |
| Application development | Python, TypeScript, JavaScript, React, Next.js, FastAPI, REST APIs |
| Machine learning | XGBoost, scikit-learn, gradient boosting, recommendation ranking, feature engineering |
| Generative AI | RAG, Ollama, local language models, evidence retrieval, citation validation |
| Data and analytics | SQL, PostgreSQL, pandas, NumPy, time-series analysis, statistical benchmarking |
| Quality and delivery | pytest, Docker, GitHub Pages, temporal validation, backtesting, retrieval evaluation |

## Current direction

I'm developing my work around grounded AI assistants, local model integration, and evaluation-driven ML applications. My next areas of exploration are tool-using AI workflows and stronger MLOps practices for reproducibility, monitoring, and deployment.

I'm interested in software, AI, and ML opportunities where I can connect thoughtful modeling with practical application development.

[Explore my repositories](https://github.com/rajashekarakula19-spec?tab=repositories)
