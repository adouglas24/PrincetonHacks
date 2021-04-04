# alGoat
Made for HackPrinceton '21.

## Inspiration
Over the past year, the field of investing has seen meteoritic growth. Individual retail investors now have serious influence over the stock market--as we all saw with GameStop. That being said, institutional investors have sophisticated technologies and approaches that the average retail investor could only dream of. We created alGOAT to help bridge that gap, empowering the everyday investor to have access to cutting-edge technologies.

## What it does
Creators can publish their trading algorithms to alGOAT. Then, alGOAT backtests the algorithm over the past 5 years of market data. This is published along with some other statistical metrics, so investors can educate themselves on the performance of algorithms while keeping the underlying code a secret. When someone invests in an algorithm, we charge a flat investment fee, to cover server costs. 
Once someone invests, the algorithm runs on our servers to determine their investments, which are automatically made on their account. They can terminate their investment at any time. Upon withdrawing funds from an algorithm, the “Creator’s Cut” of the profits, which can be determined by the algorithm creator goes to them, 3% of the profits go to the charity associated with the algorithm, and also determined by its creator, and the rest of the profits (expected to typically be in the 75%-90% range) goes to the investor. 
One key element of this model is that we do not act as a fund and the creator does not act as a financial advisor. The investor makes their own purchases, which are determined by the algorithms they chose. 

## How we built it
The frontend is a flask web app, designed in Figma and implemented using Python, HTML, and CSS. 
We created sample data and created algorithm metrics and charts in python, using NumPy and matplotlib, respectively. 
We hosted the app using a free Heroku server.  

## Challenges we ran into
One challenge that we ran into is the $25k account balance minimum requirement for day trading. We decided to incorporate algorithms that do not use day trading and algorithms that do use day trading in their implementations to allow for any investor to enter the alGOAT marketplace and start investing in algorithms.
We also ran into a challenge that our alGOAT, to become fully working, will require some network and server setup that was way beyond the scope of this weekend (see the what’s next for more info). We decided it was best to focus on fleshing out the idea and creating the UI instead of trying (and almost certainly failing) to hack together a stock exchange connection. 

## Accomplishments that we're proud of
We are particularly proud of creating a pleasant-looking, easy-to-use front end. Every member of our team had very little front-end experience, so this was something we put a particular emphasis on. 
We also are very proud of creating a business plan to go with our tech. We genuinely believe that our model, although complicated, would actually work, and will continue to work on it after this weekend. 

## What we learned
Design, design, design. We learned how to mock up a nice UI and implement it. We learned how to create not only an interesting idea but a business plan that works with governmental regulations. 

## What's next for alGOAT
First, we need to work on the servers alGOAT needs to be able to interact with the stock exchanges. We need to set up a partnership with a brokerage, so the algorithms have an endpoint to connect to. Beyond that, it’s a matter of recruiting young technologists to start making algorithms (maybe the HackPrinceton devpost will help) and then getting investors onboard (which a post on r/WallStreetBets will surely help with).
