package None;

import java.util.List;
import lombok.*;






/**
  The data element in the handle API for the status.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HdlDataStatus  {

  private String format;
  private String value;

}
