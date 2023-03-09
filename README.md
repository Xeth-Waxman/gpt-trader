# gpt-trader
A second attempt at using ChatGPT to write a complete trading website

We will (ostensibly) develop a simple-yet-complete trading website entirely using ChatGPT as an exercise in [Prompt Engineering](https://learnprompting.org/docs/intro)

The basic order of events will go like this:
1. Create a simple shell that downloads data, places it in a dataframe, performs rudimentary analysis with output
2. Create a UI with the controls necessary for a user to select a stock, a timeframe, a trading strategy, a starting amount of capital, and the ending amount of capital after running a backtest.
3. Refactor the simple shell application into a production-quality service layer
4. Wire the UI to the service layer
5. Create a CI-CD pipeline (Yes, we're going to ask ChatGPT to do ***everything***!)
6. Deploy the application into DevInt (Yes, we're going to have a Dev, QA and production environments)
7. Celebrate, drinks scotch
8. Look into adding visualizations