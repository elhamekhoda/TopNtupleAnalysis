#include "TH1F.h"

const int Nbins_r = 28;
const int Nbins_b = 18;

double rbin[Nbins_r+1] = {0, 390, 400, 410, 420, 430, 440, 450, 460, 470, 490, 510, 530, 560, 590, 620, 650, 680, 720, 770, 830, 910,  1000, 1100, 1200, 1320, 1440, 2000, 6000};
double bbin[Nbins_b+1] = {0, 480, 560, 640, 720,800, 880, 920, 970, 1040,1160,1280,1400,1700,2000,2300,2600,3000,6000};


#define PROP 0

void DoItPlease(TH1F* hin, TH1F* hout, TFile* fout, const int Nbins, double bins[], bool doValidation=true){

        double in_int = hin->Integral();


	for (unsigned int i=0; i<hin->GetNbinsX(); i++){
		float M  = hin->GetBinContent(i-1);
		float I  = hin->GetBinContent(i);	float II = I;
		float P  = hin->GetBinContent(i+1);
		float Msize = hin->GetBinWidth(i-1);
		float Isize = hin->GetBinWidth(i);
		float Psize = hin->GetBinWidth(i+1);
		if(i-1 <= 0){
			M=0.;
			Msize=0;
		}
		if(i+1 >= hin->GetNbinsX() ){
			P=0.;
			Psize=0;
		}
		float x = hin->GetBinCenter(i);
		int ix = hout->FindBin(x);
		int iy = hout->GetBinContent(ix);
		//std::cout << i << "\t" << hin->GetBinContent(i) << std::endl;
		//std::cout << i << "\t" << hin->GetNbinsX() << std::endl;
		if (I<0){
			int idif = 2;
			//std::cout << "1 " << Msize << "\t" << Isize << "\t" << Psize  << std::endl;
			while((M+I+P)<0){
			//while((M+P)<0){		// proposal 1
				if(i-idif>0) {
					M     += hin->GetBinContent(i-idif);
					Msize += hin->GetBinWidth(i-idif);
				}
				//if(i+idif < hin->GetNbinsX()) {
				if(i+idif <= hin->GetNbinsX()) { //proposal 2
					P     += hin->GetBinContent(i+idif);
					Psize += hin->GetBinWidth(i+idif);
					std::cout << hin->GetBinWidth(i+idif) << std::endl;
				}
				 //proposal 2
				else{
					Psize += hin->GetBinWidth(i-idif);// assume 0 entries in an overflow bin of the same size than the left neighbour
				
				}
				
			//std::cout << idif <<Msize << "\t" << Isize << "\t" << Psize  << std::endl;
				idif++;
			}
			II = (M+I+P)/(Msize+Isize+Psize)*Isize;
			//II = (M+P)/(Msize+Psize)*Isize;		// proposal 1
			//std::cout << Msize << "\t" << Isize << "\t" << Psize << std::endl;
			// ok but now we want to have a output histogram with fine binning
			// so we need to subtract the neigthbouring small bins
			//std::cout << "M+I+P: " << M+I+P << "\tII: " << II << "\tI:" <<  I << "\tiy: " << iy << "\t->" << II - (I-iy) << std::endl;
			II -= (I-iy);
			
			hout->SetBinContent(ix, II);
			double e = hout->GetBinError(ix);
			if (II*0.5 > e) e = II*0.5;
			hout->SetBinError(ix, e);
		}
		//if (doValidation)std::cout << i << "\t" << Msize << "\t" << Isize << "\t" << Psize << "\t" << I << "\t" << II << "\t" << II/Isize << std::endl;
	}
	
	if (doValidation){
		TCanvas* c = new TCanvas();
		
		hout->SetLineColor(9);
		hout->SetTitle(hin->GetName());
		hout->Draw();
		
		TH1F* ho = (TH1F *) hout->Rebin(Nbins, "rebin", bins);
		ho->SetLineColor(2);
		ho->Draw("same");
		hin->Draw("same");
		fout->cd();
		c->Write(hin->GetName());
		
		
		TH1F* hin2  = (TH1F*) ((TH1F*)hin->Clone())->Rebin(Nbins, "rebin", bins);
		TH1F* hout2 = (TH1F*) ((TH1F*)hout->Clone())->Rebin(Nbins, "rebin", bins);
		hin2->Scale(1.,"width");
		hout2->Scale(1.,"width");
		hin2->Draw("");
		hout2->Draw("same");
		hin2->Draw("same");
		//std::string dir = "plots_current/";
		std::string dir = "plots_proposal2/";
		std::string str = std::string(hin->GetName())+"_perGeV";
		c->Write(str.c_str());
		str = dir+std::string(hin->GetName())+"_perGeV.png";	c->Print(str.c_str());
		str = dir+std::string(hin->GetName())+"_perGeV.pdf";	c->Print(str.c_str());
		c->SetLogy();
		str = dir+std::string(hin->GetName())+"_perGeV_log.png";	c->Print(str.c_str());
		str = dir+std::string(hin->GetName())+"_perGeV_log.pdf";	c->Print(str.c_str());
		
	
	}
	double out_int = hout->Integral();
	if (out_int != 0) {
	    //hout->Scale(in_int/out_int);
	    for (int k = 0; k < hout->GetNbinsX()+1; ++k) {
	        hout->SetBinContent(k, hout->GetBinContent(k)*in_int/out_int);
  	    }
	}
	fout->cd();
	hout->Write(hout->GetName());
	
	return;
}

void copyVR(TFile *fin, TFile *fout, bool e) {
  std::vector<std::string> hname;
  std::vector<std::string> cname;
  std::vector<std::string> sname;

  hname.push_back("xlargeJetPt");
  hname.push_back("xlepPt");
  if (e) {
    cname.push_back("re1");
    cname.push_back("re2");
    cname.push_back("re3");
    cname.push_back("be1");
    cname.push_back("be2");
    cname.push_back("be3");
    sname.push_back("qcdceneup");
    sname.push_back("qcdcenedw");
    sname.push_back("qcdfwdeup");
    sname.push_back("qcdfwdedw");
  } else {
    cname.push_back("rmu1");
    cname.push_back("rmu2");
    cname.push_back("rmu3");
    cname.push_back("bmu1");
    cname.push_back("bmu2");
    cname.push_back("bmu3");
  }
  sname.push_back("");

  for (int kh = 0; kh < hname.size(); ++kh) {
    for (int kc = 0; kc < cname.size(); ++kc) {
      for (int ks = 0; ks < sname.size(); ++ks) {
        std::string n = "";
	n += hname[kh]; n+= cname[kc]; n+= sname[ks];
	TH1F *h = (TH1F *) fin->Get(n.c_str());
	if (!h) continue;
	fout->cd();
	TH1F *hclone = (TH1F *) h->Clone(n.c_str());
	fout->Write(n.c_str());
      }
    }
  }
}

void Smoothit2(){


TFile* fe =new TFile("hist_qcde.root", "READ");
TFile* fm =new TFile("hist_qcdmu.root", "READ");


TH1F* re1 = (TH1F*)fe->Get("xmttre1");
TH1F* re2 = (TH1F*)fe->Get("xmttre2");
TH1F* re3 = (TH1F*)fe->Get("xmttre3");
TH1F* rm1 = (TH1F*)fm->Get("xmttrmu1");
TH1F* rm2 = (TH1F*)fm->Get("xmttrmu2");
TH1F* rm3 = (TH1F*)fm->Get("xmttrmu3");

TH1F* be1 = (TH1F*)fe->Get("xmttbe1");
TH1F* be2 = (TH1F*)fe->Get("xmttbe2");
TH1F* be3 = (TH1F*)fe->Get("xmttbe3");
TH1F* bm1 = (TH1F*)fm->Get("xmttbmu1");
TH1F* bm2 = (TH1F*)fm->Get("xmttbmu2");
TH1F* bm3 = (TH1F*)fm->Get("xmttbmu3");

TH1F* re1cu = (TH1F*)fe->Get("xmttre1qcdceneup");
TH1F* re2cu = (TH1F*)fe->Get("xmttre2qcdceneup");
TH1F* re3cu = (TH1F*)fe->Get("xmttre3qcdceneup");
TH1F* be1cu = (TH1F*)fe->Get("xmttbe1qcdceneup");
TH1F* be2cu = (TH1F*)fe->Get("xmttbe2qcdceneup");
TH1F* be3cu = (TH1F*)fe->Get("xmttbe3qcdceneup");

TH1F* re1cd = (TH1F*)fe->Get("xmttre1qcdcenedw");
TH1F* re2cd = (TH1F*)fe->Get("xmttre2qcdcenedw");
TH1F* re3cd = (TH1F*)fe->Get("xmttre3qcdcenedw");
TH1F* be1cd = (TH1F*)fe->Get("xmttbe1qcdcenedw");
TH1F* be2cd = (TH1F*)fe->Get("xmttbe2qcdcenedw");
TH1F* be3cd = (TH1F*)fe->Get("xmttbe3qcdcenedw");

TH1F* re1fu = (TH1F*)fe->Get("xmttre1qcdfwdeup");
TH1F* re2fu = (TH1F*)fe->Get("xmttre2qcdfwdeup");
TH1F* re3fu = (TH1F*)fe->Get("xmttre3qcdfwdeup");
TH1F* be1fu = (TH1F*)fe->Get("xmttbe1qcdfwdeup");
TH1F* be2fu = (TH1F*)fe->Get("xmttbe2qcdfwdeup");
TH1F* be3fu = (TH1F*)fe->Get("xmttbe3qcdfwdeup");

TH1F* re1fd = (TH1F*)fe->Get("xmttre1qcdfwdedw");
TH1F* re2fd = (TH1F*)fe->Get("xmttre2qcdfwdedw");
TH1F* re3fd = (TH1F*)fe->Get("xmttre3qcdfwdedw");
TH1F* be1fd = (TH1F*)fe->Get("xmttbe1qcdfwdedw");
TH1F* be2fd = (TH1F*)fe->Get("xmttbe2qcdfwdedw");
TH1F* be3fd = (TH1F*)fe->Get("xmttbe3qcdfwdedw");


TH1F* re1_rebin = (TH1F*) re1->Rebin(Nbins_r, "re1_rebin", rbin);
TH1F* re2_rebin = (TH1F*) re2->Rebin(Nbins_r, "re2_rebin", rbin);
TH1F* re3_rebin = (TH1F*) re3->Rebin(Nbins_r, "re3_rebin", rbin);
TH1F* rm1_rebin = (TH1F*) rm1->Rebin(Nbins_r, "rm1_rebin", rbin);
TH1F* rm2_rebin = (TH1F*) rm2->Rebin(Nbins_r, "rm2_rebin", rbin);
TH1F* rm3_rebin = (TH1F*) rm3->Rebin(Nbins_r, "rm3_rebin", rbin);

TH1F* be1_rebin = (TH1F*) be1->Rebin(Nbins_b, "be1_rebin", bbin);
TH1F* be2_rebin = (TH1F*) be2->Rebin(Nbins_b, "be2_rebin", bbin);
TH1F* be3_rebin = (TH1F*) be3->Rebin(Nbins_b, "be3_rebin", bbin);
TH1F* bm1_rebin = (TH1F*) bm1->Rebin(Nbins_b, "bm1_rebin", bbin);
TH1F* bm2_rebin = (TH1F*) bm2->Rebin(Nbins_b, "bm2_rebin", bbin);
TH1F* bm3_rebin = (TH1F*) bm3->Rebin(Nbins_b, "bm3_rebin", bbin);

TH1F* re1cu_rebin = (TH1F*) re1cu->Rebin(Nbins_r, "re1cu_rebin", rbin);
TH1F* re2cu_rebin = (TH1F*) re2cu->Rebin(Nbins_r, "re2cu_rebin", rbin);
TH1F* re3cu_rebin = (TH1F*) re3cu->Rebin(Nbins_r, "re3cu_rebin", rbin);
TH1F* be1cu_rebin = (TH1F*) be1cu->Rebin(Nbins_b, "be1cu_rebin", bbin);
TH1F* be2cu_rebin = (TH1F*) be2cu->Rebin(Nbins_b, "be2cu_rebin", bbin);
TH1F* be3cu_rebin = (TH1F*) be3cu->Rebin(Nbins_b, "be3cu_rebin", bbin);

TH1F* re1cd_rebin = (TH1F*) re1cd->Rebin(Nbins_r, "re1cd_rebin", rbin);
TH1F* re2cd_rebin = (TH1F*) re2cd->Rebin(Nbins_r, "re2cd_rebin", rbin);
TH1F* re3cd_rebin = (TH1F*) re3cd->Rebin(Nbins_r, "re3cd_rebin", rbin);
TH1F* be1cd_rebin = (TH1F*) be1cd->Rebin(Nbins_b, "be1cd_rebin", bbin);
TH1F* be2cd_rebin = (TH1F*) be2cd->Rebin(Nbins_b, "be2cd_rebin", bbin);
TH1F* be3cd_rebin = (TH1F*) be3cd->Rebin(Nbins_b, "be3cd_rebin", bbin);

TH1F* re1fu_rebin = (TH1F*) re1fu->Rebin(Nbins_r, "re1fu_rebin", rbin);
TH1F* re2fu_rebin = (TH1F*) re2fu->Rebin(Nbins_r, "re2fu_rebin", rbin);
TH1F* re3fu_rebin = (TH1F*) re3fu->Rebin(Nbins_r, "re3fu_rebin", rbin);
TH1F* be1fu_rebin = (TH1F*) be1fu->Rebin(Nbins_b, "be1fu_rebin", bbin);
TH1F* be2fu_rebin = (TH1F*) be2fu->Rebin(Nbins_b, "be2fu_rebin", bbin);
TH1F* be3fu_rebin = (TH1F*) be3fu->Rebin(Nbins_b, "be3fu_rebin", bbin);

TH1F* re1fd_rebin = (TH1F*) re1fd->Rebin(Nbins_r, "re1fd_rebin", rbin);
TH1F* re2fd_rebin = (TH1F*) re2fd->Rebin(Nbins_r, "re2fd_rebin", rbin);
TH1F* re3fd_rebin = (TH1F*) re3fd->Rebin(Nbins_r, "re3fd_rebin", rbin);
TH1F* be1fd_rebin = (TH1F*) be1fd->Rebin(Nbins_b, "be1fd_rebin", bbin);
TH1F* be2fd_rebin = (TH1F*) be2fd->Rebin(Nbins_b, "be2fd_rebin", bbin);
TH1F* be3fd_rebin = (TH1F*) be3fd->Rebin(Nbins_b, "be3fd_rebin", bbin);

TH1F* re1_rebin2 = (TH1F*)re1->Clone("xmttre1");
TH1F* re2_rebin2 = (TH1F*)re2->Clone("xmttre2");
TH1F* re3_rebin2 = (TH1F*)re3->Clone("xmttre3");
TH1F* rm1_rebin2 = (TH1F*)rm1->Clone("xmttrmu1");
TH1F* rm2_rebin2 = (TH1F*)rm2->Clone("xmttrmu2");
TH1F* rm3_rebin2 = (TH1F*)rm3->Clone("xmttrmu3");

TH1F* be1_rebin2 = (TH1F*)be1->Clone("xmttbe1");
TH1F* be2_rebin2 = (TH1F*)be2->Clone("xmttbe2");
TH1F* be3_rebin2 = (TH1F*)be3->Clone("xmttbe3");
TH1F* bm1_rebin2 = (TH1F*)bm1->Clone("xmttbmu1");
TH1F* bm2_rebin2 = (TH1F*)bm2->Clone("xmttbmu2");
TH1F* bm3_rebin2 = (TH1F*)bm3->Clone("xmttbmu3");

TH1F* re1cu_rebin2 = (TH1F*)re1cu->Clone("xmttre1qcdceneup");
TH1F* re2cu_rebin2 = (TH1F*)re2cu->Clone("xmttre2qcdceneup");
TH1F* re3cu_rebin2 = (TH1F*)re3cu->Clone("xmttre3qcdceneup");
TH1F* be1cu_rebin2 = (TH1F*)be1cu->Clone("xmttbe1qcdceneup");
TH1F* be2cu_rebin2 = (TH1F*)be2cu->Clone("xmttbe2qcdceneup");
TH1F* be3cu_rebin2 = (TH1F*)be3cu->Clone("xmttbe3qcdceneup");

TH1F* re1cd_rebin2 = (TH1F*)re1cd->Clone("xmttre1qcdcenedw");
TH1F* re2cd_rebin2 = (TH1F*)re2cd->Clone("xmttre2qcdcenedw");
TH1F* re3cd_rebin2 = (TH1F*)re3cd->Clone("xmttre3qcdcenedw");
TH1F* be1cd_rebin2 = (TH1F*)be1cd->Clone("xmttbe1qcdcenedw");
TH1F* be2cd_rebin2 = (TH1F*)be2cd->Clone("xmttbe2qcdcenedw");
TH1F* be3cd_rebin2 = (TH1F*)be3cd->Clone("xmttbe3qcdcenedw");

TH1F* re1fu_rebin2 = (TH1F*)re1fu->Clone("xmttre1qcdfwdeup");
TH1F* re2fu_rebin2 = (TH1F*)re2fu->Clone("xmttre2qcdfwdeup");
TH1F* re3fu_rebin2 = (TH1F*)re3fu->Clone("xmttre3qcdfwdeup");
TH1F* be1fu_rebin2 = (TH1F*)be1fu->Clone("xmttbe1qcdfwdeup");
TH1F* be2fu_rebin2 = (TH1F*)be2fu->Clone("xmttbe2qcdfwdeup");
TH1F* be3fu_rebin2 = (TH1F*)be3fu->Clone("xmttbe3qcdfwdeup");

TH1F* re1fd_rebin2 = (TH1F*)re1fd->Clone("xmttre1qcdfwdedw");
TH1F* re2fd_rebin2 = (TH1F*)re2fd->Clone("xmttre2qcdfwdedw");
TH1F* re3fd_rebin2 = (TH1F*)re3fd->Clone("xmttre3qcdfwdedw");
TH1F* be1fd_rebin2 = (TH1F*)be1fd->Clone("xmttbe1qcdfwdedw");
TH1F* be2fd_rebin2 = (TH1F*)be2fd->Clone("xmttbe2qcdfwdedw");
TH1F* be3fd_rebin2 = (TH1F*)be3fd->Clone("xmttbe3qcdfwdedw");


TFile *foute = new TFile("hist_qcde_qcdfixzero2.root", "RECREATE");
TFile *foutm = new TFile("hist_qcdmu_qcdfixzero2.root", "RECREATE");
DoItPlease(re1_rebin, re1_rebin2, foute, Nbins_r, rbin);
DoItPlease(re2_rebin, re2_rebin2, foute, Nbins_r, rbin);
DoItPlease(re3_rebin, re3_rebin2, foute, Nbins_r, rbin);

DoItPlease(rm1_rebin, rm1_rebin2, foutm, Nbins_r, rbin);
DoItPlease(rm2_rebin, rm2_rebin2, foutm, Nbins_r, rbin);
DoItPlease(rm3_rebin, rm3_rebin2, foutm, Nbins_r, rbin);

DoItPlease(be1_rebin, be1_rebin2, foute, Nbins_b, bbin);
DoItPlease(be2_rebin, be2_rebin2, foute, Nbins_b, bbin);
DoItPlease(be3_rebin, be3_rebin2, foute, Nbins_b, bbin);

DoItPlease(bm1_rebin, bm1_rebin2, foutm, Nbins_b, bbin);
DoItPlease(bm2_rebin, bm2_rebin2, foutm, Nbins_b, bbin);
DoItPlease(bm3_rebin, bm3_rebin2, foutm, Nbins_b, bbin);

DoItPlease(re1cu_rebin, re1cu_rebin2, foute, Nbins_r, rbin);
DoItPlease(re2cu_rebin, re2cu_rebin2, foute, Nbins_r, rbin);
DoItPlease(re3cu_rebin, re3cu_rebin2, foute, Nbins_r, rbin);
DoItPlease(be1cu_rebin, be1cu_rebin2, foute, Nbins_b, bbin);
DoItPlease(be2cu_rebin, be2cu_rebin2, foute, Nbins_b, bbin);
DoItPlease(be3cu_rebin, be3cu_rebin2, foute, Nbins_b, bbin);

DoItPlease(re1cd_rebin, re1cd_rebin2, foute, Nbins_r, rbin);
DoItPlease(re2cd_rebin, re2cd_rebin2, foute, Nbins_r, rbin);
DoItPlease(re3cd_rebin, re3cd_rebin2, foute, Nbins_r, rbin);
DoItPlease(be1cd_rebin, be1cd_rebin2, foute, Nbins_b, bbin);
DoItPlease(be2cd_rebin, be2cd_rebin2, foute, Nbins_b, bbin);
DoItPlease(be3cd_rebin, be3cd_rebin2, foute, Nbins_b, bbin);

DoItPlease(re1fu_rebin, re1fu_rebin2, foute, Nbins_r, rbin);
DoItPlease(re2fu_rebin, re2fu_rebin2, foute, Nbins_r, rbin);
DoItPlease(re3fu_rebin, re3fu_rebin2, foute, Nbins_r, rbin);
DoItPlease(be1fu_rebin, be1fu_rebin2, foute, Nbins_b, bbin);
DoItPlease(be2fu_rebin, be2fu_rebin2, foute, Nbins_b, bbin);
DoItPlease(be3fu_rebin, be3fu_rebin2, foute, Nbins_b, bbin);

DoItPlease(re1fd_rebin, re1fd_rebin2, foute, Nbins_r, rbin);
DoItPlease(re2fd_rebin, re2fd_rebin2, foute, Nbins_r, rbin);
DoItPlease(re3fd_rebin, re3fd_rebin2, foute, Nbins_r, rbin);
DoItPlease(be1fd_rebin, be1fd_rebin2, foute, Nbins_b, bbin);
DoItPlease(be2fd_rebin, be2fd_rebin2, foute, Nbins_b, bbin);
DoItPlease(be3fd_rebin, be3fd_rebin2, foute, Nbins_b, bbin);

copyVR(fe, foute, true);
copyVR(fm, foutm, false);

foute->Close();
foutm->Close();


}
