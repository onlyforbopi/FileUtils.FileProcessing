package FPrcs_Pckg_Main;

use strict;
use warnings;

use Readonly;
use Exporter;

# Globals.
#
# Constants.
Readonly my    $CHK_VAL => "È";
Readonly my    $CHK_FRM => 39; #! Offset 0 !
Readonly my    $CHK_LEN => 1;
#
# FILES.
#
# FILES' NAMES.
#
# INPUT.
my $file_name_in;
# OUTPUT: From file_name_ot above.
my $file_name_ot;
#
# FILES' HANDLES.
#
# INPUT: Declare.
my $file_hndl_in;
# OUTPUT: Declare.
my $file_hndl_ot;
#
   
our @ISA = qw( Exporter );
# Exported Functions.
our @EXPORT = qw( filePrcs ); # These are exported by default.

# # our @EXPORT = qw( filePrcs loadFltr2Table cmprBase2Fltr); # These are exported by default.
# #
# # our @EXPORT_OK = qw( loadFltr2Table cmprBase2Fltr); # These can be exported.
# #

# Variables.
#

# Functions' Prototypes. # "forward declaration".
#
sub filePrcs;
sub doWork;

# Functions' Body.
#
sub filePrcs
{
   # FILES' NAMES.
   #
   # ***!!! 
   # ***!!! ASSSUMING PROVIDED --> CHECKED in RUN Job. !!!***
   # ***!!!
   #
   # INPUT: From subroutine's Parameters.
   $file_name_in = $_[0];
   # OUTPUT: From file_name_ot above.
   $file_name_ot = $_[1];
   
   print "file_name_in: $file_name_in\n";
   print "file_name_ot: $file_name_ot\n";
   
   # FILES' HANDLES.
   #
   # INPUT FILES: Open.
   open $file_hndl_in, '<', $file_name_in;
   # OUTPUT FILES: Open.
   open $file_hndl_ot, '>', $file_name_ot;
   
   doWork();

   # INPUT FILES: Close.
   close $file_hndl_in;
   # OUTPUT FILES: Open.
   close $file_hndl_ot;
      
   return (0);

}
# filePrcs  ends.

sub doWork
{
   my ($line, $srch);
   
   # Read File_In.
   while ($line = <$file_hndl_in>) 
   {
      # Get search value.
      $srch = substr("$line", $CHK_FRM, $CHK_LEN); #! Offset 0 !
      
      # If equal.
      if ($srch eq $CHK_VAL) #! string-wise search !
      {
         # Write input line to output file.
         print {$file_hndl_ot} "$line";
      }
   }

   return (0);
}
# doWork ends.

1;
