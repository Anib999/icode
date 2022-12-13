from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import IndustryType, CompanyDetails
from .forms import IndustryTypeForm, CompanyDetailsForm

# Create your views here.


def index(request):
    queryString = request.GET.get('q') if request.GET.get('q') != None else ''
    industryQueryString = request.GET.get('filterByIndustry') if request.GET.get('filterByIndustry') != None else ''

    print(industryQueryString == '')

    industryList = IndustryType.objects.all()
    industryWithCompany = {industry.industry_name: []
                           for industry in industryList}

    if industryQueryString == '' or industryQueryString == '0':
        companyListFilter = CompanyDetails.objects.filter(
            Q(company_name__icontains=queryString) |
            Q(owner_name__icontains=queryString) |
            Q(address__icontains=queryString) |
            Q(email_address__icontains=queryString) |
            Q(contact_no__icontains=queryString) |
            Q(industrytype__industry_name__icontains=queryString)
        )
    else:
        companyListFilter = CompanyDetails.objects.filter(
            Q(industrytype__industry_name__iexact=industryQueryString)
        )

    for company in companyListFilter:
        industryTypeStr = str(company.industrytype)
        singleCompanyDetail = {
            'cid': company.id,
            'company_name': company.company_name,
            'owner_name': company.owner_name,
            'address': company.address,
            'email_address': company.email_address,
            'contact_no': company.contact_no,
        }
        industryWithCompany[industryTypeStr].append(singleCompanyDetail)

    context = {'industryList': industryList,
        'industryWithCompany': industryWithCompany, 'queryString': queryString, 'industryQueryString': industryQueryString}
    return render(request, 'industryapp/index.html', context)


def storeIndustryType(request):
    industryList = IndustryType.objects.all()
    # form = IndustryTypeForm()
    if request.method == 'POST':
        form = IndustryTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('storeIndustryType')
        else:
            messages.error(
                request, 'Industry name not saved. Please try again')
    context = {'industryList': industryList, 'butName': 'Save'}
    # 'form': form
    return render(request, 'industryapp/industrytype.html', context)


def editIndustryType(request, pk):
    industryList = IndustryType.objects.all()
    industrySingle = IndustryType.objects.get(id=pk)
    if request.method == 'POST':
        form = IndustryTypeForm(request.POST)
        if form.is_valid():
            industrySingle.industry_name = request.POST.get('industry_name')
            industrySingle.save()
            return redirect('storeIndustryType')
        else:
            messages.error(
                request, 'Industry name not saved. Please try again')
    context = {'industryList': industryList, 'industrySingle': industrySingle, 'pk': pk, 'butName': 'Edit'}
    return render(request, 'industryapp/industrytype.html', context)


def storeCompanyDetails(request):
    # form = CompanyDetailsForm()
    industryList = IndustryType.objects.all()
    if request.method == 'POST':
        form = CompanyDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('storeCompanyDetails')
        else:
            messages.error(
                request, 'Company details not saved. Please try again')
    # 'form': form,
    context = {'industryList': industryList, 'butName': 'Save'}
    return render(request, 'industryapp/companydetails.html', context)


def editCompanyDetails(request, pk):
    singleCompanyDetails = CompanyDetails.objects.get(id=pk)
    industryList = IndustryType.objects.all()
    if request.method == 'POST':
        form = CompanyDetailsForm(request.POST)
        if form.is_valid():
            iType = IndustryType.objects.get(id=request.POST.get('industrytype'))
            singleCompanyDetails.industrytype = iType
            singleCompanyDetails.company_name = request.POST.get('company_name')
            singleCompanyDetails.owner_name = request.POST.get('owner_name')
            singleCompanyDetails.address = request.POST.get('address')
            singleCompanyDetails.email_address = request.POST.get('email_address')
            singleCompanyDetails.contact_no = request.POST.get('contact_no')
            singleCompanyDetails.save()
            return redirect('index')
        else:
            messages.error(
                request, 'Company details not updated. Please try again')
    context = {'singleCompanyDetails': singleCompanyDetails, 'industryList': industryList, 'pk': pk, 'butName': 'Edit'}
    return render(request, 'industryapp/companydetails.html', context)

def deleteCompanyDetails(request, pk):
    singleCompanyDetails = CompanyDetails.objects.get(id=pk)
    singleCompanyDetails.delete()
    return redirect('index')