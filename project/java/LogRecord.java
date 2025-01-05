package None;

import java.util.List;
import lombok.*;






/**
  A log record for changes made on a PID4CatRecord starting from registration.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LogRecord  {

  private String datetimeLog;
  private Agent hasAgent;
  private String changedField;
  private String description;

}