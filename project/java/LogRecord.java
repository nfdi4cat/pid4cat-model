package None;

import java.util.List;
import lombok.*;






/**
  A log record for changes made in a pid4cat handle record starting from registration.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LogRecord  {

  private ZonedDateTime datetimeLog;
  private Agent hasAgent;
  private String changedField;
  private String description;

}
