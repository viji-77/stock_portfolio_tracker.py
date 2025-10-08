# stock_portfolio_tracker.py

Appends Data

Each new run can be modified to append data to the existing CSV file instead of overwriting it.
This allows users to track portfolio growth over multiple sessions, maintaining a continuous investment record.

Calculation and Tracking

Manual Input: Users enter stock symbols and quantities directly in the terminal.
Hardcoded Prices: A predefined dictionary stores stock prices (e.g., {"AAPL": 180, "TSLA": 250}).
Automatic Calculation: The program multiplies each stock’s price by its quantity to compute the total investment value.

A clear summary displays each stock’s details along with the overall total investment.

Data Saving

Flexible Output Options:
Results can be saved as either a .txt or .csv file.
Persistent Storage:
Saved files are easy to open, share, and reuse in Excel or other tools for further analysis.

Scheduling Tasks (Optional Enhancement)

Automation with Schedule:
The application can be extended using the schedule library to run automatically at specific intervals — for example, to update and log portfolio data every hour or every day.

Infinite Loop:
By implementing a continuous loop, the application can execute scheduled calculations on time, keeping portfolio data up to date without manual input.

Why This Application Stands Out

Automated Portfolio Updates
Eliminate the need for manual calculations by introducing scheduling for automatic updates and data logging.

Organized Investment Records
Keep all investment details in a structured, time-stamped CSV file for easy tracking and historical analysis.

Simple and Scalable
Easily modify the script to include real-time stock prices, additional data fields, or automated scheduling intervals.

Why Build or Use This Application?

For Developers:
A great project to practice:

Python fundamentals (dictionary, loops, file handling)

Basic financial calculations

Optional automation using the schedule library

For Users:
An efficient tool for tracking personal stock investments — whether manually or automatically.
It provides an easy way to calculate and store investment data without relying on external APIs or complex financial software.
