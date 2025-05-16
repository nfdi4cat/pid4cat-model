package None;

import java.util.List;
import lombok.*;



/* version: 0.3.0.post26.dev0+e73dc8d */


/**
  Data class for a change log of modification made on a pid4cat handle record starting from its registration.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LogRecord  {

  private ZonedDateTime datetimeLog;
  private Agent hasAgent;
  private String changedField;
  private String description;

}
