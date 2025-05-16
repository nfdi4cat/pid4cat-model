package None;

import java.util.List;
import lombok.*;



/* version: 0.3.0.post26.dev0+e73dc8d */


/**
  The data class for the change log.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HdlDataLog  {

  private String format;
  private List<LogRecord> value;

}
