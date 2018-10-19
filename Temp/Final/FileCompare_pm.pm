package FileCompare_pm;

###################################################################################################
# Filter = file_hndl_fltr
# Base = file_hndl_base
# Script will check which lines of Filter exist in the base
# If line of filter exists in base then print line of base to YESHAVE4
# If line of filter doesnt exit in base then print line of base to NOHAVE4
#
#
# Version :
# Checked for greek font, substring before / after greek / tabs
# filter, base
#
# How to use :
# Run with PERL_UNICODE=S perl script.pl
# DOES NOT WORK IF THE INPUT FILES CONTAIN TABS. / NEEDS EXPAND ON LINUX
# --
# expand -t4 infile > outfile
# PERL_UNICODE=S perl script.pl
#
# t4 : because n++ views tab as 4 spaces.
#####################################################################################################

# # Uses.
# #use strict;
# #use warnings;
# # use autodie;
# # use Encode;
# # use utf8;
# use Text::Tabs;
# # use Text::Unidecode;
# # Text:Unidecode would also solve this problem but needs special installation
# # Encode; is necessary for decode_utf8
# # Alternate version : Use $ARGS[0,1...] so that user can supply input files as parameters (TO DO)
# use Readonly;

# Uses.
use Exporter;
use Text::Tabs;

# Globals.
my    $THIS_NAME = $0 . " package 02";

# Script start.
print $THIS_NAME, " started\n";

our @ISA= qw( Exporter );

# # these CAN be exported.
# our @EXPORT_OK = qw( export_me export_me_too );

# these are exported by default.
our @EXPORT = qw( fileCmpr );

sub fileCmpr
{
   # FILES' NAMES.
   #
   # INPUT: From subroutine's Parameters, *Assuming* provided...
   my $file_name_fltr = $_[0];
   my $file_name_base = $_[1];
   #
   # OUTPUT: From file_name_base above.
   my $file_name_xstY = $file_name_base . ".xstY";
   my $file_name_xstN = $file_name_base . ".xstN";;
   
   print "FILE_OT_xstY: $file_name_xstY\n";
   print "FILE_OT_xstN: $file_name_xstN\n";
   #
   # FILES' HANDLES.
   # INPUT: Declare.
   my $file_hndl_fltr;
   my $file_hndl_base;
   #
   # OUTPUT: Declare.
   my $file_hndl_xstY;
   my $file_hndl_xstN;
   #
   # OUTPUT: Open.
   open $file_hndl_xstY, '>', $file_name_xstY;
   open $file_hndl_xstN, '>', $file_name_xstN;
   #

   # This sets the STDOUT so that it can support unicode characters
   # STDOUT is normally a non-unicode handle
   # binmode(STDOUT, ":utf8");

   # VARIABLES - Initialize variables
   my $arrayinit = "X";
   my %results;
   my $srch;
   my $chek;

   ##################################################################						
   # Open Filter - read lines
   open $file_hndl_fltr, '<', $file_name_fltr;
   while (my $line = <$file_hndl_fltr>) 
   {

      # Remove trailing new line and white space characters
      chomp($line);
      
      # decode_utf8 tells perl that the string contains Unicode data in UTF-8 encoding
      # $line = decode_utf8( $line );
      
      # Convert tabs to spaces
      $line = expand($line);
      
      # Substring loaded into filter (Offset 0! - Always one less than n++)
      my $load = substr("$line", 0, 3);
      #start from digit, length of string
      
      # Print substring load for check purposes! (TEST)
      print "$load \n";
      
      # Increment hash for each string loaded
      $results{$load}++
      
      # my $results{$load} = $arrayinit;
      # $results{$load} = "$arrayinit";
   }							

   ##############################################################################

   # Separate filter load values from base search values (TEST)
   print "@@@@@@@@@@@@@@@@@\n";

   ##############################################################################
   # Open base, read lines
   open $file_hndl_base, '<', $file_name_base;
   # open ( my $file_hndl_base, "<:utf8", $file_hndl_base);												
   while (my $line = <$file_hndl_base>) 
   {

      # Remove trailing new line
       chomp($line);
      
      # decode_utf8 tells perl that the string contains Unicode data in UTF-8 encoding
      # $line = decode_utf8( "$line" );
      
      # Convert tabs to spaces
      $line = expand($line);
      
      # Value to search for, e.g. [0..29]
      # (Offset 0! - Always one less than n++)
      my $srch = substr("$line", 139, 3);
      
      # my $srch = Encode::decode( 'iso-8859-1', $srch );
      # Print substring on base for check purposes! (TEST)
      # print "$srch \n";
      
      # my $srch = "substr($line, 0, 30)"; # ?mOno gia to an uparxoun kena sthn arxg h sto telos?
      # chek = results[0..29]
      
      # Assign to substring search to variable check
      my $chek = $results{$srch};
      # my $chek = "$results{$srch}";
      
      # Control block on check.
      if ($chek >= 1) # string compare.
      {
      
      # We use this command to get rid of the "Wide character in print" warning perl gives
      # It can be used with STDOUT or appropriate filehandle, and perl will treat it as UTF-8 capable
      # binmode($file_hndl_xstY, ":utf8");
      
      # Print output line and trailing new line 
      print {$file_hndl_xstY} "$line\n";
      }
      else
      {
      # print file_hndl_xstN "$line";
      # print file_hndl_xstN $line;
      
      # We use this command to get rid of the "Wide character in print" warning perl gives
      # It can be used with STDOUT or appropriate filehandle, and perl will treat it as UTF-8 capable
      # binmode($file_hndl_xstN, ":utf8");
      
      # Print output line and trailing new line
      print {$file_hndl_xstN} "$line\n";
      }
   }
   
   return (0);
} # fileCmpr  ends.

##########################################################################
# Script end.   
print $THIS_NAME, " ended\n";
#
