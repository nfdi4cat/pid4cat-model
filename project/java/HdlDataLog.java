package None;

import java.util.List;
import lombok.*;






/**
  The data element in the handle API for the change log.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HdlDataLog  {

  private String format;
  private List<LogRecord> value;

}
