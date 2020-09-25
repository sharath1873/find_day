from django.shortcuts import render

def home(request):
	return render(request,'bornday/home.html')

def which_day(request):
	d = int(request.GET.get('day'))
	m = int(request.GET.get('month'))
	y = int(request.GET.get('year'))
	l = [d,m,y]
	find_odd = odd_days(request,y-1)
	mo = 0
	mmm = 0
	no_leap_yr = [0,3,0,3,2,3,2,3,3,2,3,2,3]
	leap_yr = [0,3,1,3,2,3,2,3,3,2,3,2,3]
	if(y%4==0):
		for i in range(0,m):
			mo += leap_yr[i]
		week_day = (find_odd+mo+d)%7
		if(week_day==0):
			return render(request,'bornday/which_day.html',{'res':'Sunday'})
		elif(week_day==1):
			return render(request,'bornday/which_day.html',{'res':'Monday'})
		elif(week_day==2):
			return render(request,'bornday/which_day.html',{'res':'Tuesday'})
		elif(week_day==3):
			return render(request,'bornday/which_day.html',{'res':'Wednesday'})
		elif(week_day==4):
			return render(request,'bornday/which_day.html',{'res':'Thursday'})
		elif(week_day==5):
			return render(request,'bornday/which_day.html',{'res':'Friday'})
		elif(week_day==6):
			return render(request,'bornday/which_day.html',{'res':'Saturday'})
	else:
		for i in range(0,m):
			mmm += no_leap_yr[i]
		week_day = (find_odd+mmm+d)%7
		if(week_day==0):
			return render(request,'bornday/which_day.html',{'res':'Sunday'})
		elif(week_day==1):
			return render(request,'bornday/which_day.html',{'res':'Monday'})
		elif(week_day==2):
			return render(request,'bornday/which_day.html',{'res':'Tuesday'})
		elif(week_day==3):
			return render(request,'bornday/which_day.html',{'res':'Wednesday'})
		elif(week_day==4):
			return render(request,'bornday/which_day.html',{'res':'Thursday'})
		elif(week_day==5):
			return render(request,'bornday/which_day.html',{'res':'Friday'})
		elif(week_day==6):
			return render(request,'bornday/which_day.html',{'res':'Saturday'})
	

def odd_days(request,y):
	if(y>=400):
		fr_y = y//400
		fr_mod = y-fr_y*400
		on_yy = fr_mod//100
		one_odd_day = (5*on_yy)%7
		on_mod = fr_mod%100
		leap = on_mod//4 #leap for under 99 years
		nrml_y = on_mod - leap
		calcu_odd = nrml_y+(leap+leap)
		n_odd = calcu_odd%7
	return one_odd_day+n_odd

	
