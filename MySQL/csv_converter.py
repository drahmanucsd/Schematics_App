import csv

# Specify the input CSV file and output text file paths
csv_file_path = 'sample.csv'
text_file_path = 'csvdata.sql'

# Open the CSV file for reading
with open(csv_file_path, 'r') as csv_file:
    # Create a CSV reader
    csv_reader = csv.reader(csv_file)
    
    # Open the text file for writing
    with open(text_file_path, 'w') as text_file:
        # Iterate through each row in the CSV file
        for index, row in enumerate(csv_reader):
            # Construct the line to be written to the text file
            row[0] = index
            line = "INSERT IGNORE Data (Column1, AIR_MOTOR, APPROVED_BY, CHS, CUST, DATE_DRAWN, DESCR, DIRNAME, DRAWING_NUMBER, DRAWN_BY, DWG_TYPE, ELEC_MOTOR, EM_LOCKOUT, EM_SEQUENCING, EM_SINGLE_PILOT_SOURCE, EM_FAIL_OPEN, EM_LOW_TRIP_POSITION, R, S, T, U, V, W, X, Y, Z, AA, AB, AC, AD, AE, AF, AG, AH, AI, AJ, AK, AL, AM, AN, AO, AP, AQ, AR, A_S, A_T, AU, AV, AW, AX, AY, AZ, BA, BB, BC, BD, BE, BF, BG, BH, BI, BJ, BK, BL, BM, BN, BO, BP, BQ, BR, BS, BT, BU, BV, BW, BX, B_Y, BZ, CA, CB, CC, CD, CE, CF, CG, CH, CI, CJ, CK, CL, CM, CN, CO, CP, CQ, CR, CS, CT, CU, CV, CW, CX, CY, CZ, DA, DB, DC, DD, DE, DF, DG, DH, DI, DJ, DK, DL, DM, DN, DO, DP, DQ, DR, DS, DT, DU, DV, DW, DX, DY, DZ, EA, EB, E_C, E_D, E_E, E_F, E_G, EH, EI, EJ, EK, EL, EM, EN, EO, EP, EQ, ER, ES, ET, EU, EV, EW, EX, EY, EZ, FA, FB, FC, FD, FE, FF, FG, FH, FI, FJ, FK, FL, FM, FN, FO, FP, FQ, FR, FS, FT, FU, FV, FW, FX, FY) VALUES (" + ', '.join([f"'{cell}'" for cell in row]) + ");"
            # Write the line to the text file
            if index >30:
                text_file.write(line + '\n')

print(f"Text file '{text_file_path}' has been created.")
