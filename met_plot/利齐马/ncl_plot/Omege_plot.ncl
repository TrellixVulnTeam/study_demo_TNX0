begin
;>---------------------------------------<
;            data　change
;>---------------------------------------<
;filetime = "gdas1.fnl0p25.2019081000.f00"

;time = "2019080806"
time = "2019080912"
;time = "2019081000"
;time = "2019081006"


;中心的经纬度




;lat0 = 23.50
;lon0 = 125.00

lat0 = 27.75
lon0 = 122.25

;lat0 = 29.00
;lon0 = 120.50

;lat0 = 29.75
;lon0 = 119.75

;lat0 = 30.00
;lon0 = 119.00

wks = gsn_open_wks("png",time+"_omega")
f = addfile("/home/liyuan3970/Data/data/meto_data/fnl/fnl_025/gdas1.fnl0p25."+time + ".f00.grib2", "r")

;>---------------------------------------<
;             COMPUTE DATA 
;>---------------------------------------<
v = f->VGRD_P0_L100_GLL0(10:30,:,:)
u = f->UGRD_P0_L100_GLL0(10:30,:,:)
w = f->VVEL_P0_L100_GLL0
hgt = f->HGT_P0_L100_GLL0(:, :, :)
rh = f->RH_P0_L100_GLL0(:, :, :)
t = f->TMP_P0_L100_GLL0(:, :, :)
printVarSummary(hgt)
printVarSummary(rh)
printVarSummary(t)
printVarSummary(u)
lev1 = f->lv_ISBL5
;lev2 = f->lv_ISBL0
;print(lev1)




h = new((/31,721,1440/),typeof(hgt))
p = (/100,200,300,500,700,1000,2000,3000,5000,7000,10000,15000,20000,25000,30000,35000,40000,45000,50000,55000,60000,65000,70000,75000,80000,85000,90000,92500,95000,97500,100000/)
print(dimsizes(p))
p2=conform_dims((/31,721,1440/), p, 0)
printVarSummary(p2)




h(0:5,:,:)=hgt(1:6,:,:)
h(6:7,:,:)=hgt(8:9,:,:)
h(8:30,:,:)=hgt(11:33,:,:)
;printVarSummary(h)

temp = new((/31,721,1440/),typeof(t))
temp(0:5,:,:)=t(1:6,:,:)
temp(6:7,:,:)=t(8:9,:,:)
temp(8:30,:,:)=t(11:33,:,:)
;printVarSummary(temp)


ept=pot_temp_equiv(p2, temp, rh, 1, "rh") 
printVarSummary(ept)
duv=uv2dv_cfd(u,v,u&lat_0,u&lon_0,2)
;duv = uv2dvF_Wrap(u,v)
copy_VarCoords(u, duv)
printVarSummary(duv)
;>---------------------------------------<
;             DATA OUTPUT
;>---------------------------------------<

ept1 = ept({lv_ISBL0|10000:100000},{lat_0|lat0},{lon_0|118:126})
u1 = u({lv_ISBL5|:},{lat_0|lat0},{lon_0|118:126})  ;lat0.25 * lon0.25   ---->25N127.5E
v1 = v({lv_ISBL5|:},{lat_0|lat0},{lon_0|118:126})
w1 = w({lv_ISBL9|:},{lat_0|lat0},{lon_0|118:126})

duv1 = duv({lv_ISBL5|:},{lat_0|lat0},{lon_0|118:126})
duv1 = duv1*10000

w1 = w1 *-100

ept2 = ept({lv_ISBL0|10000:100000},{lat_0|20:35},{lon_0|lon0})
u2 = u({lv_ISBL5|:},{lat_0|20:35},{lon_0|lon0})  ;lat0.25 * lon0.25   ---->25N127.5E
v2 = v({lv_ISBL5|:},{lat_0|20:35},{lon_0|lon0})
w2 = w({lv_ISBL9|:},{lat_0|20:35},{lon_0|lon0})
duv2 = duv({lv_ISBL5|:},{lat_0|20:35},{lon_0|lon0})
duv2 = duv2*10000
printVarSummary(ept2)
printVarSummary(u2)
printVarSummary(duv2)
printVarSummary(w2)
w2 = w2 *-100


print("ok")

vcres=True
  vcres@vcLineArrowColor        = "black"        ; change vector color
  ;vcres@vcGlyphStyle = "WindBarb"
  vcres@gsnDraw = False
  vcres@gsnFrame = False
  ;vcres@vcLineArrowThicknessF   = 2.0               ; change vector thickness
  vcres@vcRefAnnoOn  =False
  vcres@vcRefAnnoArrowUseVecColor    =False ;Ref颜色独立
  vcres@vcRefAnnoPerimOn =False
  vcres@vcRefAnnoArrowLineColor="black"
  vcres@vcRefAnnoString1              ="2m/s" ;Ref框里写字
  vcres@vcRefAnnoFontHeightF  =0.02
  vcres@vcRefAnnoFontThicknessF =0.02
  vcres@vcRefAnnoJust    =      "TopRight"
  vcres@vcMapDirection   = False
  vcres@vcRefAnnoString2   =" "           ;去掉reference vector字样
  ;vcres@vcRefMagnitudeF           = 2            ; define vector ref mag
  vcres@vcRefLengthF              = 0.15          ; define length of vec ref
  vcres@vcRefAnnoOrthogonalPosF   =-1.36 ;;;-1.36            ; move ref vector
  ;vcres@vcMin
  ;vcres@vcMaxMagnitudeF  = 10
  vcres@vcMinDistanceF            =0.025
  vcres@vcMinFracLengthF    = 0.2
  vcres@vcLineArrowThicknessF =1.3
  vcres@gsnPresHgtHeightLabelOn = False
  vcres@vcVectorDrawOrder       = "PostDraw"        ; draw vectors last



  ;------------------------------------------------------
  ;                       plot
  ;
  ;------------------------------------------------------
vcres@cnFillOn = True
vcres@cnLinesOn = False
;vcres@cnLineLabelsOn = False
;vcres@cnInfoLabelOn = False
;vcres@lbLabelBarOn = True;False
  
vcres@cnLevelSelectionMode="ManualLevels"
vcres@cnMinLevelValF=-2
vcres@cnMaxLevelValF=4
vcres@cnLevelSpacingF=1
vcres@cnFillColors = (/34,78,114,0,148,162,178,215,225/)
vcres@lbLabelBarOn = False
vcres@tiYAxisString   = " "
vcres@gsnLeftString   = "Vertical Wind";
vcres@gsnRightString = " "
vcres@cnInfoLabelOn=False



plots = new(2,graphic)


vcres1 = vcres
vcres1@gsnLeftString   = "";
vcres1@tmXBValues=(/118,119,120,121,122,123,124,125,126/)
vcres1@tmXBLabels=(/"118E","119E","120E","121E","122E","123E","124E","125E","126E"/)
vcres2 = vcres
vcres2@gsnLeftString   = "";
vcres2@tmXBValues=(/20,22,24,26,28,30,32,34/)
vcres2@tmXBLabels=(/"20N","22N","24N","26N","28N","30N","32N","34N"/)

cnres = True
cnres@gsnDraw = False
cnres@gsnFrame = False
cnres@cnSmoothingOn = True ;
cnres@cnSmoothingDistanceF   = 0.001
cnres@cnLevelSelectionMode   = "ManualLevels"
cnres@cnMinLevelValF = 300
cnres@cnMaxLevelValF = 400
cnres@cnLevelSpacingF = 4
cnres@cnInfoLabelOn = False
cnres@trYReverse = True  ;坐标轴反转
cnres@cnLineLabelsOn          =  True
cnres@cnLineLabelFontHeightF = 0.01
cnres@cnLineThicknessF = 3.0
cnres@cnLineLabelInterval = 1
cnres@cnLineColor = "red"
cnres@gsnLeftString   = time;
cnres@gsnPresHgtHeightLabelOn = False
cnplots = new(2,graphic)
cnplots(0) = gsn_csm_pres_hgt(wks, ept1, cnres)
cnplots(1) = gsn_csm_pres_hgt(wks, ept2, cnres) 
;gsn_csm_pres_hgt
;cnplots(0) = gsn_csm_contour(wks, ept1, cnres)
;cnplots(1) = gsn_csm_contour(wks, ept2, cnres) 

plots(0) = gsn_csm_pres_hgt_vector(wks,duv1,u1,w1,vcres1)  
plots(1) = gsn_csm_pres_hgt_vector(wks,duv2,v2,w2,vcres2) 

overlay(plots(0),cnplots(0))
overlay(plots(1),cnplots(1))
;overlay(cnplots(0),plots(0))
;overlay(cnplots(1),plots(1))
 pres1                     = True
  pres1@gsnPanelTop       =1
  pres1@gsnPanelBottom    =0.4
  ;pres1@gsnPanelLeft      =0
  ;pres1@gsnPanelRight     = 0.6  
  pres1@gsnFrame            = False      ; don't advance frame yet
  pres1@gsnPanelLabelBar    = True       ; common label bar
  pres1@gsnPanelFigureStrings = (/"a","b"/)
  ;pres1@lbOrientation       ="Vertical"
  pres1@amJust  = "TopLeft"
gsn_panel(wks,plots,(/1,2/),pres1)
;gsn_panel(wks,cnplots,(/1,2/),pres1)
;draw(plots)
frame(wks)










end