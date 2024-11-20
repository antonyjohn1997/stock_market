from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json

    if request.method == 'POST':
        # ticker = request.POST['ticker_symbol']
        ticker = request.POST['ticker']
        
        api_request=requests.get("https://api.twelvedata.com/quote?symbol=" + ticker + "&apikey=7aa493ac340a40c4bfdcc4237397e42e")
    
        try:
           #api_request= requests.get("https://api.twelvedata.com/time_series?symbol=AAPL&interval=1min&apikey=7aa493ac340a40c4bfdcc4237397e42e")
           api = json.loads(api_request.content)
        except Exception as e:
           api = "Error ..."
        return render(request, 'home.html', {'api': api})    
      
    else:
        return render(request, 'home.html', {'ticker': "Enter a ticker symbol above..."})    
    
    
     
    
def about(request):
    return render(request, 'about.html',{})    