
function imggen = ecg2cwt()
ecg_signal_data = csvread('../filtered/saurabh2.csv')
ecgdata = ecg_signal_data';
signallength = 900;
cwtfb = cwtfilterbank('SignalLength',signallength, 'Wavelet','amor','VoicesPerOctave',12);
nol = 900;
colormap = jet(128);
folderpath = strcat('testing\');
ecgsignal = ecgdata(1 , 1 : nol);
cfs = abs(cwtfb.wt(ecgsignal));
im = ind2rgb(im2uint8(rescale(cfs)), colormap);         
filename = strcat(folderpath, sprintf('44.jpg', 1));
imwrite(imresize(im, [227 227]), filename);          
end