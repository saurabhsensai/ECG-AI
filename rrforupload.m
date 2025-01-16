function result = rrforupload(csvFileName)
    filewithpath = fullfile('static', csvFileName);
    Fs = 180;

    % Read CSV file
    ecg_signal = csvread(filewithpath);
    ecg_signal_data = ecg_signal';

    t = 1:length(ecg_signal_data);
    tx = t ./ Fs;


    % Assuming ecgsig should be derived from ecg_signal_data
    wt = modwt(ecg_signal_data, 4, 'sym4');
    wtrec = zeros(size(wt));
    wtrec(3:4, :) = wt(3:4, :);

    y = imodwt(wtrec, 'sym4');
    y = abs(y).^2;
    avg = mean(y);

    % Use peak detection to find R-peaks
    [Rpeaks, locs] = findpeaks(y, t, 'MinPeakHeight', 8 * avg, 'MinPeakDistance', 50);
    nohb = length(locs);

    % Calculate heart rate per minute
    timelimit = length(ecg_signal_data) / Fs;
    hbpermin = (nohb * 60) / timelimit;

    % Calculate RR intervals
    rr_intervals = diff(locs);
    std_value = std(rr_intervals);
    
    % Display or use rr_intervals as needed

    % Create a structure to hold the results
    result.avg_rr_intervals = mean(rr_intervals);
    result.hbpermin = hbpermin;
    result.std_value = std_value ;
end
