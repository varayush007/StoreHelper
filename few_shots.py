few_shots = [
    # done
    {
        'Question': "How many white color Nike extra small size tshirt do we have?",
        'SQLQuery': "SELECT stock_quantity FROM t_shirts WHERE color='White' AND size='XS' AND brand='Nike'",
        'SQLResult': "Result of the SQL query",
        'Answer': "79"
    },
    # done
    {
        'Question': "What is the cost of all inventory of brand levi in red color",
        'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color = 'Red'",
        'SQLResult': "Result of the SQL query",
        'Answer': "130"
    },
    # done
    {
        'Question': "What is the discounted amount of red color levi in M size",
        'SQLQuery': "SELECT price * (1 - discounts.pct_discount) AS discounted_amount FROM t_shirts JOIN discounts ON t_shirts.t_shirt_id = discounts.t_shirt_id WHERE color = 'Red' AND size = 'M' AND t_shirts.brand = 'Levi';",
        'SQLResult': "Result of the SQL query",
        'Answer': "No results were found in the db. Would you like to try a different search or refine your query?"
    },
    # done
    {
        'Question': "What is the percentage discount of red color levi in M size",
        'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color = 'Red'",
        'SQLResult': "Result of the SQL query",
        'Answer': "No results were found in the db. Would you like to try a different search or refine your query?"

    },
    # done
    {
        'Question': "If we have to sell all the Levi’s T-shirts today with discounts applied. How much revenue  our store will generate (post discounts)?",
        'SQLQuery': """SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
                    (select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Levi'
                    group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id""",
        'SQLResult': "Result of the SQL query",
        'Answer': "23508"
    },
    # done
    {
        'Question': "How many nike black color tshirts are available in the store",
        'SQLQuery': "SELECT sum(stock_quantity) FROM t_shirts WHERE color = 'Black' AND brand = 'Nike'",
        'SQLResult': "Result of the SQL query",
        'Answer': "345"
    }
]