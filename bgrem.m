%This function takes in a matrix containing spectral data (spectra), a window for the SNIP algorithm, and an 
%order (order) and window (window) for the Savitzky–Golay filter used within. 
%It returns the spectra with background removed (bgremd), along with the removed component (bg). 
function [bgremd, bg] = bgrem(spectra,window,order,sgw)
    %Rows of spectra = individual measurements, columns = wavenumbers,
    %elements are filled with CCD charge intensity (proportional to light intesnity)
    [rows, cols] = size(spectra);
    %We need to create a padded version of the spectra that adds mirrors to the 
    %beginning and end of the spectrum a length equal to the window.
    %This is so we can remove the background at the edges of the spectrum too.
    %index 1 in spectra will be a = w+1 in padded version
    w = floor(window/2);
    a = w+1;
    %Index end in spectra will be b = end + w in padded version.
    b = cols+w;
    padded = zeros(cols + 2*w,rows);
    padded(a:b,:) = spectra.';
    %Mirrored ends of padded matrix is the reflected difference.
    for i = 1:w
        padded(a-i,:) = 2.*padded(a,:) - padded(a+i,:);
        padded(b+i,:) = 2.*padded(b,:) - padded(b-i,:);
    end
    %Smooth padded dataset with a Savitzky–Golay filter
    padded(:,:) = sgolayfilt(padded,order,sgw);

    %Now apply SNIP (1st order) algorithm...
    %The SNIP algorithm iteratively determines a baseline to subtract from 
    %the spectrum by finding the minimum between a given point and the
    %average value of the outer edges of a window centered on that point.
    for j = w:-1:1
        padded(a:b,:) = min(padded(a:b,:),(padded(a-j:b-j,:) + padded(a+j:b+j,:))./2);
    end
    bg = padded(a:b,:).';
    bgremd = spectra - bg;
end %End of function
