# technion-GS-support
Support scripts for Technion use with GradeScope.

* process_submissions.py: Takes a submissions.zip file downloaded
  from GradeScrope and replaces the fonts so that Hebrew renders,
  and apply Bidi to fix the direction. It outputs the modified files
  in the structure needed by the Technion (ID/exam-code/Color.pdf).
  * This script should be considered a derivative work of
    https://github.com/pymupdf/PyMuPDF-Utilities/blob/master/font-replacement/repl-font.py
