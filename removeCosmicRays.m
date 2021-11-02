%This function takes in a matrix containing multiple spectral measurements (spectra), 
%a specified peak multiple which is undesirable (C), and a specified 
%order (order) and window (framelen) for a Savitzky–Golay filter to be used. It 
%returns the spectra with cosmic rays removed (fixed), along with information 
%on the cosmic rays (crays, count).
function [fixed,crays,count] = removeCosmicRays(spectra,C,order,framelen)

fixed = zeros(size(spectra));
fixed(:,:) = spectra;
weights = ones(1,framelen);%vector of ones for sgolay filter weights

%Take the median and absolute difference of spectra to sort them
med = median(fixed);
absdiff = abs(fixed-med);
sort_absdiff = sort(absdiff,'descend');

%Specify the cosmic rays as greater than the specified multiple "C"
smad = sort_absdiff(2,:); %new
cosmic_rays = absdiff > C*smad;
count = nnz(cosmic_rays);
crays = false(size(cosmic_rays));
crays(:,:) = cosmic_rays;
%Find the cosmic rays position
nf = any(cosmic_rays,2);

%Loop to find any cosmic rays and replace them with a sgolay filter alternative.
midpoint = floor(framelen/2 + 1);
stop = midpoint/2;
w = 1;
while any(nf)
    %specify weight for sgolay filt to ignore the cosmic ray
    weights(1,midpoint-w:midpoint+w) = 0.0001;
    %specify filtered alternative for cosmic ray locations
    sg = sgolayfilt(fixed(nf,:),order,framelen,weights,2);
    inds = find(nf);
    for i = 1:length(inds)
        %Replace the cosmic rays with the filtered alternative
        fixed(inds(i),cosmic_rays(inds(i),:)) = sg(i,cosmic_rays(inds(i),:));
    end
    %Re-specify the difference order, and check for cosmic rays again 
    med(1,:) = median(fixed);
    absdiff(:,:) = abs(fixed-med);
    %Re-specify what the second highest peak intensity is now
    smad(1,:) = max(absdiff(absdiff < max(absdiff)));
    %Re-specify cosmic rays
    cosmic_rays(:,:) = absdiff > C*smad;
    nf(:) = any(cosmic_rays,2);
    w = w+1;%Expand the window of ignoring weights if the cosmic rays have 
    %survived the loop. Break the loop once you have passed the allotted
    %window length, or there are no more cosmic rays.

    if w > stop
        break
    end  
end
end %End of function